class Student:

    def __init__(self, name, last_name, birth_year):
        self.name = name
        self.last_name = last_name
        self.birth_year = birth_year
        # calculate the id here
        self.id = name[0] + last_name + birth_year


object_name = input()
object_last_name = input()
object_year = input()
test = Student(object_name, object_last_name, object_year)
print(test.id)
