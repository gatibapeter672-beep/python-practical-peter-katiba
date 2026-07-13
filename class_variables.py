class Student:
    school = "Cooperative University"

    def __init__(self, name):
        self.name = name

s1 = Student("Peter")
s2 = Student("John")

print(s1.name, s1.school)
print(s2.name, s2.school)