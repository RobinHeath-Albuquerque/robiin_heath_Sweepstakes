from stack import Stack


class StackManager:
    def __init__(self, stack):
        self.stack = ()

    def push(self):
        print(f'push from {self.stack}')

    def pop(self):
        print(f'pop from {self.stack}')
