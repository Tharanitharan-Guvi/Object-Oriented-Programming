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
        print(f"Marks: {self.marks} and Name: {self.name}")


s1 = DEF("Suresh", 80)
s1.display()