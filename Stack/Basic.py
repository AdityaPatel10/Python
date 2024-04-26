class Stack:
    def __init__(self):
        self.items = []
    def is_empty(self):
        return len(self.items) == 0
    def push(self, item):
        self.items.append(item)
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Stack is empty")
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Stack is empty")
    def size(self):
        return len(self.items)
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3) 
stack.push(4)
stack.push(5)
print("Stack Size is: ",stack.size())
stack.pop()
stack.pop()
print("Stack Items are: ",stack.items)
print("Last item in the stack is: ", stack.peek())
print("Stack Size is: ",stack.size())