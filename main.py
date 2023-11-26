class Students:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def __str__(self):
        return f"Name: {self.name} and Marks : {self.marks}"
    
    @classmethod
    def newConstructor(cls, studentList):
        studentObjList = []
        for student in studentList:
            name, marks = student
            studentObjList.append(cls(name, marks))
            cls.display()
        return studentObjList

    @staticmethod
    def display():
        print("The student is succesfully added")


studentList = [["Suresh", 80], ["Ramesh", 85], ["Arjun", 90]]
objList = Students.newConstructor(studentList)

for obj in objList:
    print(obj)