

def read_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer!")


class Student:
    def __init__(self,name,id,dob):
        self.name = name
        self.id = id
        self.dob = dob
        self.mark = {}

    def addMark(self,id_course,mark):
        self.mark[id_course]=mark

    def showInfor(self):
        print(f"Name: {self.name}, Id: {self.id}, DOB: {self.dob}")

class Course:
    def __init__(self,name,id):
        self.name =name
        self.id = id

    def showInfor(self):
        print(f"Name: {self.name} Id: {self.id}")

class Student_Managements:
    def __init__(self):
        self.student = {}
        self.course ={}


    def inputStudent(self): 
        nb_student = read_int("Enter the number of student: ")
        for i in range(nb_student):
            name = input(f"Enter the name of the {i+1}th student: ")
            id = read_int(f"Enter the id of {name}: ")

            if id in self.student:
                print("Student ID already exists!")
                continue

            dob = input(f"Enter the dob of {name}: ")
            self.student[id] =Student(name,id,dob)
            print("-"*100)


    def inputCourse(self):
        nb_course = read_int("Enter the number of course: ")
        for i in range(nb_course):
            name = input(f"Enter the name of the {i+1}th course: ")
            id = read_int(f"Enter the id of {name}:" )

            if id in self.course:
                print("Course ID already exists!")
                continue
            self.course[id] = Course(name,id)
            print("-"*100)


    def inputMark(self):
        id_course = read_int("Enter the course id that you want to enter mark: ")

        if id_course not in self.course:
            print("Course does not exist!")
            return

        id_student =read_int("Enter the student id that you want to enter mark: ")

        if id_student not in self.student:
            print("Student does not exist!")
            return
        
        
        mark = list(map(float, input(f"Enter the mark for student {id_student} in course {id_course}: ").split()))
        self.student[id_student].addMark(id_course,mark)
        

    def listCourses(self):
        if not self.course:
                print("Empty")
        else:
            print("ALL COURSES ARE: ")
            for course in self.course.values():
                course.showInfor()
          

    def listStudents(self):
        if not self.student:
                print("Empty")
        else:
            print("ALL STUDENT ARE: ")
            for student in self.student.values():
                student.showInfor()


    def show_All_Mark(self):
        id_course = read_int("Enter the id course that you want to see mark of student: ")

        if id_course not in self.course:
            print("Course does not exist!")
            return
        
        print(f"All mark of student in this course:")
        for student in self.student.values():
            mark = student.mark.get(id_course)
            print(f"Name: {student.name}, Id: {student.id}, DOB: {student.dob}, Mark: {mark}")

    def show_Only_Mark(self):
        id_course = read_int("Enter the id course that you want to see mark: ")
        if id_course not in self.course:
            print("Course does not exist!")
            return
        course = self.course[id_course]
        
        id_student = read_int("Enter the id student that you want to see mark: ")
        if id_student not in self.student:
            print("Student does not exist!")
            return
        student = self.student[id_student]
        mark = student.mark.get(id_course)


        print(f"The mark of {course.name} ({course.id}) of {student.name} is: mark")

        
    

    def run(self):
        while True:
            print("="*100)
            print("""STUDENT MANAGEMENT""")
            print("1. Input information about student")
            print("2. Input information about course")
            print("3. Input the mark of course")
            print("4. Show all student")
            print("5. Show all course")
            print("6. Show all mark of course")
            print("7. Show mark student")
            print("8. Nothing and exit")
            n = read_int("Choice: ")
            print("="*100)

            if n == 8:
                print("Goodbye!")
                break
            if n == 1:
                self.inputStudent()
            if n == 2:
                self.inputCourse()
            if n == 3:
                self.inputMark()
            if n == 4:
                self.listStudents()
            if n == 5:
                self.listCourses()
            if n == 6 :
                self.show_All_Mark()
            if n==7:
                self.show_Only_Mark()


if __name__  == "__main__":
    app = Student_Managements()
    app.run()


