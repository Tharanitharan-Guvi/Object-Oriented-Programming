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

## Destructor
It is called when an object is to be destroyed

```python

class Student:

    # constructor method
    def __init__(self, n, marks):
        self.name = n
        self.marks = marks

    def display(self):
        print(f"Name : {self.name}, and Marks: {self.marks}")
    
    # Destructor
    def __del__(self):
        print(f"Student : {self.name} is removed from the system")

student1 = Student("Suresh", 90)
student1.display()
del student1
student1.display()
```


## Dunder Methods
Dunder methods are also known as magic methods or special methods and they are used to perform some special behaviors.

```python

# Addition +        -->     __add__()
# Subtraction -     -->     __sub__()
# Multiplication *  -->     __mul__()
# Less than <       -->     __lt__()

class Vector:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __add__(self, other):
        return (self.x + other.x, self.y + other.y)

v1 = Vector(10, 20)
v2 = Vector(30, 40)
print(v1 + v2)

```

## Class Methods and Static Methods:

- Class Method: A method that is bound to the class and not the object, the instance of the class.

- Static Method: A method that is not bound to the class or the objects.

```python

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

'''
Output:
The student is succesfully added
The student is succesfully added
The student is succesfully added
Name: Suresh and Marks : 80
Name: Ramesh and Marks : 85
Name: Arjun and Marks : 90
'''
```

## Four Pillars of OOP

### Encapsulation

It describes the idea of wrapping data and the methods within one unit.

### Abstraction

It is the process of hiding the internal details of an application from the outer world

#### Private Methods

The methods which are only accessed within the class and cannot be accessed outside the class. But python doesn't support true private methods. The private method can be acessed by this '_NameOfTheClass__methodName'.

```python

class Students:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Display 1")
        self.__display()
    
    def __display(self):
        print("Display 2")

s1 = Students("Suresh", 80)
s1.display()
s1._Students__display()
s1.__display()


'''
Display 1
Display 2
Display 2
Traceback (most recent call last):
  File "E:\Guvi\PAT Sessions\OOP\main.py", line 16, in <module>
    s1.__display()
    ^^^^^^^^^^^^
AttributeError: 'Students' object has no attribute '__display'. Did you mean: 'display'?
'''
```

### Polymorphism
It is the condition of occurrence in different forms.

### Inheritance

Inheritance allows us to create a new class from an existing class. We are going to derive all the methods and attributes from the parent/super class to the child/sub class.

Syntax:

```python
class Superclass:
    pass

class Subclass(Superclass):
    pass
```

Example:

```python

class ABC:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __str__(self):
        return f"Name: {self.name} and Marks: {self.marks}"

    def display(self):
        print(f"Name: {self.name} and Marks: {self.marks}")

class DEF(ABC):
    def display(self):
        super().display()

s1 = DEF("Suresh", 80)
s1.display()
```

### Types of Inheritance:

1. Simple Inheritance:

```python

class Parent:
    pass

class Child(Parent):
    pass

```

2. Multilevel Inheritance:

```python
class Grandfather:
    pass

class father(Grandfather):
    pass

class son(father):
    pass
```

3. Multiple Inheritance:

```python

class A:
    pass

class B:
    pass

class C(A, B):
    pass
```

#### Uses of Inheritance:
1. This allows for code reusability.
2. This allows for cleaner code and easier to maintain.