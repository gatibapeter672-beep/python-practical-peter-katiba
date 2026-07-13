class Student:
    school = "Coop University"

    def __init__(self, name):
        self.name = name

    @classmethod
    def change_school(cls, new_name):
        cls.school = new_name


print(Student.school)


Student.change_school("New University")


print(Student.school)