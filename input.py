from domains import Student, Course

def read_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer!")




def inputStudent(student): 
    nb_student = read_int("Enter the number of student: ")
    for i in range(nb_student):
        name = input(f"Enter the name of the {i+1}th student: ")
        id = read_int(f"Enter the id of {name}: ")

        if id in student:
            print("Student ID already exists!")
            continue

        dob = input(f"Enter the dob of {name}: ")
        student[id] =Student(name,id,dob)
        print("-"*100)


def inputCourse(course):
    nb_course = read_int("Enter the number of course: ")
    for i in range(nb_course):
        name = input(f"Enter the name of the {i+1}th course: ")
        id = read_int(f"Enter the id of {name}:" )
        credit = read_int(f"Enter the credit of {name}:")

        if id in course:
            print("Course ID already exists!")
            continue
        course[id] = Course(name,id,credit)
        print("-"*100)


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
    