from domains import Student, Course
import os
import zipfile


FILES = ["students.txt", "courses.txt", "marks.txt"]
def compress_data():
    with zipfile.ZipFile("students.dat","w",zipfile.ZIP_DEFLATED) as z:
        for name in FILES:
            if os.path.exists(name):
                z.write(name)

def decompress_data():
    if not os.path.exists("students.dat"):
        return False
    with zipfile.ZipFile("students.dat") as z:
        z.extractall()
    return True

def load_students(student):
    if not os.path.exists("students.txt"):
        return
    with open("students.txt", encoding="utf-8") as f:
        for line in f:
            name, id, dob = line.strip().split(",")
            student[int(id)] = Student(name, int(id), dob)

def load_courses(course):
    if not os.path.exists("courses.txt"):
        return
    with open("courses.txt",encoding="utf-8") as f:
        for line in f:
            name, id, credit =line.strip().split(",")
            course[int(id)] = Course(name, int(id), credit)

def load_marks(student):
    if not os.path.exists("mark.txt"):
        return
    with open("marks.txt",encoding="utf-8") as f:
        for line in f:
            id_student, id_course, marks= line.strip().split(",")
            if int(id_student) in student:
               student[int(id_student)].addMark(int(id_course), [float(m) for m in marks.split()])

def read_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer!")


def saveStudents(student):
    with open("students.txt","w",encoding="utf-8") as f:
        for s in student.values():
            f.write(f"{s.name}, {s.id}, {s.dob}\n")

def save_courses(course):
    with open("courses.txt", "w", encoding="utf-8") as f:
        for c in course.values():
            f.write(f" {c.name}, {c.id}, {c.credit}\n")


def save_marks(student):
    with open("mark.txt","w",encoding="utf-8") as f:
        for s in student.values():
            for id_course, mark in s.mark.items():
                marks_str = " ".join(str(m) for m in mark)
                f.write(f"Student_ID: {s.id}, Course_ID: {id_course}, Mark: {marks_str}\n")
            

def inputStudent(student): 
    nb_student = read_int("Enter the number of student: ")
    for i in range(nb_student):
        name = input(f"Enter the name of the {i+1}th student: ").strip()
        id = read_int(f"Enter the id of {name}: ")

        if id in student:
            print("Student ID already exists!")
            continue

        dob = input(f"Enter the dob of {name}: ")
        student[id] =Student(name,id,dob)
        print("-"*100)
    saveStudents(student)


def inputCourse(course):
    nb_course = read_int("Enter the number of course: ")
    for i in range(nb_course):
        name = input(f"Enter the name of the {i+1}th course: ").strip()
        id = read_int(f"Enter the id of {name}:" )
        credit = read_int(f"Enter the credit of {name}:")

        if id in course:
            print("Course ID already exists!")
            continue
        course[id] = Course(name,id,credit)
        print("-"*100)
    save_courses(course)


def inputMark(student,course):
    id_course = read_int("Enter the course id that you want to enter mark: ")

    if id_course not in course:
        print("Course does not exist!")
        return

    id_student =read_int("Enter the student id that you want to enter mark: ")

    if id_student not in student:
        print("Student does not exist!")
        return
    
    
    mark = list(map(float, input(f"Enter the mark for student {id_student} in course {id_course}: ").split()))
    student[id_student].addMark(id_course,mark)
    save_marks(student)
    