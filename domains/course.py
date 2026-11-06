class Course:
    def __init__(self,name,id,credit):
        self.name =name
        self.id = id
        self.credit = credit

    def showInfor(self):
        print(f"Name: {self.name}, Id: {self.id}")
