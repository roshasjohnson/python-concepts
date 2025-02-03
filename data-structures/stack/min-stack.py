
class MinStack:
    stack  = []

    def push(self,val):
        self.stack.append(val) 
    
    def pop(self):
        if self.stack:
            return self.stack.pop()
        else:
            return "No elements"

    def top(self):
        if self.stack:
            return self.stack[-1]
        else:
            return "No elements"

    def getMin(self):
        return min(self.stack)
    
    def display(self):
        return self.stack

stack = MinStack()
stack.push(3)
stack.push(5)
print(stack.getMin())  # Output: 3
stack.push(1)
print(stack.getMin())  # Output: 1
stack.pop()
stack.push(2)
stack.push(10)
print(stack.getMin())  # Output: 3

print(MinStack.stack)