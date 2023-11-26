# Object Oriented Programming

Python is a versatile language, it supports both functional programming and Object Oriented Programming.


## Difference between FP and OOP:

- Functions : Focuses on functions as the primary building blocks.
- OOP: Focuses on objects, which encapsulate both data and their actions.

## Class:
A class is considered as a blueprint of objects.

## Objects:
Object are instance of a class.


### Define Python Class and Create a Object

Syntax:

```python

class ClassName:
    # Class definition

Objname = ClassName()
```

Example:

```python

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
```


## Constructor

The construction method is called whenever a new object of that class is instantiated.

```python

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
```