student = {}
course ={}


def inputStudent(): 
    nb_student = int(input("Enter the number of student: "))
    for i in range(nb_student):
        name = input(f"Enter the name of the {i+1}th student: ")
        id = int(input(f"Enter the id of {name}: "))
        dob = input(f"Enter the dob of {name}: ")
        student[id] ={"infor":(name,dob),"course":{}}
        print("-"*100)
        


def inputCourse():
    nb_course = int(input("Enter the number of course: "))
    for i in range(nb_course):
        name = input(f"Enter the name of the {i+1}th course: ")
        id = int(input(f"Enter the id of {name}:" ))
        course[id] ={"name": name, "mark":[]}
        print("-"*100)


def inputMark():
    id_course = int(input("Enter the course id that you want to enter mark: "))

    if id_course not in course:
        print("Course does not exist!")
        return

    id_student =int(input("Enter the student id that you want to enter mark: "))

    if id_student not in student:
        print("Student does not exist!")
        return
    
    
    mark = list(map(float, input(f"Enter the mark for student {id_student} in course {id_course}: ").split()))
    student[id_student]["course"][id_course] = {
        "name": course[id_course]['name'],
        "mark": mark
    }
    print("-"*100)


def listCourses():
    print("ALL COURSES ARE: ")

    if not course:
        print("Empty")

    for key, value in course.items():
        print(f"Name of course: {value["name"]}, Id: {key}")
    print("-"*100)

def listStudents():
    print("ALL STUDENT ARE: ")

    if not student:
        print("Empty")
    
    for key, value in student.items():
        print(f"Name: {value["infor"][0]}, Id: {key}, Dob: {value["infor"][1]}")


def show_All_Mark():
    id_course = int(input("Enter the id course that you want to see mark of student: "))

    if id_course not in course:
        print("Course does not exist!")
        return
    
    for key, value in student.items(): 
        print(f"Id: {key}, Name: {value["infor"][0]}, Dob: {value["infor"][1]}, mark: {value["course"][id_course]["mark"]} ")
    print(student)


while True:
    print("="*100)
    print("""STUDENT MANAGEMENT""")
    print("1. Input information about student")
    print("2. Input information about course")
    print("3. Input the mark of course")
    print("4. Show all student")
    print("5. Show all course")
    print("6. Show all mark of course")
    print("7. Nothing and exit")
    n = int(input("Choice: "))
    print("="*100)

    if n == 7:
        break
    if n == 1:
        inputStudent()
    if n == 2:
        inputCourse()
    if n == 3:
        inputMark()
    if n == 4:
       listStudents()
    if n == 5:
        listCourses()
    if n == 6 :
        show_All_Mark()
    
    




