def read_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer!")


def menu():
    print("=" * 100)
    print("STUDENT MANAGEMENT")
    print("1. Input information about student")
    print("2. Input information about course")
    print("3. Input the mark of course")
    print("4. Show all student")
    print("5. Show all course")
    print("6. Show all mark of course")
    print("7. Show mark student")
    print("8. Nothing and exit")
    n = read_int("Choice: ")
    return n
    print("="*100)

   

def listCourses(course):
    if not course:
            print("Empty")
    else:
        print("ALL COURSES ARE: ")
        for course in course.values():
            course.showInfor()
    

def listStudents(student):
    if not student:
            print("Empty")
    else:
        print("ALL STUDENT ARE: ")
        for student in student.values():
            student.showInfor()


def show_All_Mark(student,course):
    id_course = read_int("Enter the id course that you want to see mark of student: ")

    if id_course not in course:
        print("Course does not exist!")
        return
    
    print(f"All mark of student in this course:")
    for student in student.values():
        mark = student.mark.get(id_course)
        print(f"Name: {student.name}, Id: {student.id}, DOB: {student.dob}, Mark: {mark}")

def show_Only_Mark(student,course):
    id_course = read_int("Enter the id course that you want to see mark: ")
    if id_course not in course:
        print("Course does not exist!")
        return
    course = course[id_course]
    
    id_student = read_int("Enter the id student that you want to see mark: ")
    if id_student not in student:
        print("Student does not exist!")
        return
    student = student[id_student]
    mark = student.mark.get(id_course)


    print(f"The mark of {course.name} ({course.id}) of {student.name} is: {mark}")


def calculate_GPA():
    pass
        
    
