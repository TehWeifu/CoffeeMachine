class Person:
    def __init__(self, name):
        self.name = name

    # create the method greet here
    def greet(self):
        print("Hello, I am {}!".format(self.name))


test_name = input()
test = Person(test_name)
test.greet()
