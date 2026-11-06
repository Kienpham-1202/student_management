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