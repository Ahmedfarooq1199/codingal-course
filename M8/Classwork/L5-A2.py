class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class Student(Person):
    def __init__(self, fname, lname, year):
        Person.__init__(self,fname, lname)
        self.graduationyear = year


    
x = Student("Mike", "Olsen", 2024)
x.printname()
print(x.graduationyear)
    