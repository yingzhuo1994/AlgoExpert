# Feel free to add new properties and methods to the class.
class MinMaxStack:
    def __init__(self):
        self.stack = []
        self.minStack = []
        self.maxStack = []


    def peek(self):
        # Write your code here.
        if self.stack:
            return self.stack[-1]
        else:
            return None

    def pop(self):
        # Write your code here.
        if self.stack:
            self.minStack.pop()
            self.maxStack.pop()
            return self.stack.pop()
        else:
            return None

    def push(self, number):
        # Write your code here.
        self.stack.append(number)
        if self.minStack:
            self.minStack.append(min(number, self.minStack[-1]))
        else:
            self.minStack.append(number)
        if self.maxStack:
            self.maxStack.append(max(number, self.maxStack[-1]))
        else:
            self.maxStack.append(number)

    def getMin(self):
        # Write your code here.
        if self.minStack:
            return self.minStack[-1]
        else:
            return None

    def getMax(self):
        # Write your code here.
        if self.maxStack:
            return self.maxStack[-1]
        else:
            return None
