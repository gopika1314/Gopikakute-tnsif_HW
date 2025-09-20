class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack += [item]