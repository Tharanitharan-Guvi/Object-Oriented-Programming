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