import input as inp
import output as out

student = {}
course = {}

print("Checking students.dat...")
if inp.decompress_data():
    print("Decompressed OK")
    inp.load_students(student)
    inp.load_courses(course)
    inp.load_marks(student)
    print(f"Loaded {len(student)} students, {len(course)} courses")
else:
    print("students.dat not found")
while True:
    n = out.menu()

    if n == 8:
        inp.compress_data()
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
