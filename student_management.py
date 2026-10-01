student = {}
course ={}
#Input function
#InforStudent
def inputStudent():
    print("="*100)
    nb_student = int(input("Enter the number of Student:"))
    for i in range(nb_student):
        name = input("Enter the name:")
        id = input(f"Enter the student id of {name}:")
        dob = input(f"Enter the DOB of {name}:")
        student[id] = {"info":(name,dob),"course":course}
    return student

# inputcourse function
def inputCourse():
    print("="*100)
    nb_course = int(input("Enter the number of Course:"))
    for i in range(nb_course):
       name_course = input(f"Enter the name of the {i+1}th course:")
       id_course = input(f"Enter the course Id of {name_course}:")
       course[id_course]={"name":name_course,"mark":[]}
    return student


#select course and enter mark
def select():
    print("="*100)
    select_course_id = input("Enter the course id you want to enter mark:")
    select_student_id = input("Enter the student id that you want to enter mark:")
    mark = float(input(f"Enter the mark of {select_course_id}:"))
    student[select_student_id]["course"][select_course_id]["mark"] = mark


#list course
def list_course():
    print("="*100)
    print("ALL COURSE ARE:")
    for key, value in course.items():
        print(f"{value["name"]}")


#list students
def list_students():
    print("="*100)
    print("ALL STUDENT ARE:")
    for key, value in student.items():
        print(f"{value["info"][0]}")

#show_student_mark
def show_student_mark():
    print("="*100)
    select_course_id = input("Enter the course id you want to see mark:")
    select_student_id = input("Enter the student id that you want to see mark:")
    print(f"{student[select_student_id]["course"][select_course_id]["mark"]}") 



while True:
    print("="*100)
    print("""STUDENT MANAGEMENT""")
    print("1. Input information about student")
    print("2. Input information about course")
    print("3. Input the mark of course")
    print("4. Show all student")
    print("5. Show all course")
    print("6. Show mark")
    print("7. Nothing and exit")
    
    n = int(input("What do you want?: "))
    if n == 7:
        break
    if n == 1:
        inputStudent()
    if n == 2:
        inputCourse()
    if n == 3:
        select()
    if n == 4:
        list_students()
    if n == 5:
        list_course()
    if n == 6 :
        show_student_mark()
    


