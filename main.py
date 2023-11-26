class Student:
    name = ""
    marks = 0

    def display(self):
        print(f"Name : {self.name} and Marks: {self.marks}\n")

student1 = Student()
student1.name = "Suresh"
student1.marks = 90
student1.display()

student2 = Student()
student2.display()

'''
Output:

Name : Suresh and Marks: 90

Name :  and Marks: 0

'''