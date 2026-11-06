import input as inp
import output as out

student = {}
course = {}

while True:
    n = out.menu()

    if n == 8:
        print("Goodbye!")
        break
    elif n == 1:
        inp.inputStudent(student)
    elif n == 2:
        inp.inputCourse(course)
    elif n == 3:
        inp.inputMark(student, course)
    elif n == 4:
        out.listStudents(student)
    elif n == 5:
        out.listCourses(course)
    elif n == 6:
        out.show_All_Mark(student,course)
    elif n == 7:
       out.show_Only_Mark(student,course)
    else:
        print("Enter the number from 1-8!")
