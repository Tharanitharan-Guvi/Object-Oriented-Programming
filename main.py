class Student:

    # constructor
    def __init__(self, n, marks):
        self.name = n
        self.marks = marks

    def display(self):
        print(f"Name : {self.name}, and Marks: {self.marks}")

student1 = Student("Suresh", 90)
student1.display()

student2 = Student("Ramesh", 80)
student2.display()

'''
Output:
Name : Suresh, and Marks: 90
Name : Ramesh, and Marks: 80
'''