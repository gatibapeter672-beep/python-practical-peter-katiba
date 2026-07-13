class Student:
    def __init__(self, name, adm, course):
        self.name = name
        self.adm = adm
        self.course = course

    def display(self):
        print(self.name, self.adm, self.course)


s1 = Student("Peter", "123", "CS")
s2 = Student("John", "124", "IT")
s3 = Student("Mary", "125", "SE")

s1.display()
s2.display()
s3.display()