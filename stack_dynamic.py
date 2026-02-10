# 3. LINEAR - DYNAMIC (Stack)
# Classification: Linear -> Dynamic -> Stack (LIFO)

class Stack:
    def __init__(self):
        self.elements = []
    
    def push(self, data):
        self.elements.append(data)
        
    def pop(self):
        if not self.is_empty():
            return self.elements.pop()
        return "Stack is empty"

    def is_empty(self):
        return len(self.elements) == 0

# Usage
my_stack = Stack()
my_stack.push("Action 1")
my_stack.push("Action 2")
print(f"Stack LIFO Pop: {my_stack.pop()}") # Action 2 comes out first
