class Stack():

    def __init__(self):
        self.list = []

    def push(self, el):
        self.list.append(el)

    def pop(self):
        return self.list.pop(-1)

    def peek(self):
        return self.list[len(self.list) - 1]

    def is_empty(self):
        if self.list == []:
            return True
        else:
            return False
