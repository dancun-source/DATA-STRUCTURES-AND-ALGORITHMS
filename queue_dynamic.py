# 4. LINEAR - DYNAMIC (Queue)
# Classification: Linear -> Dynamic -> Queue (FIFO)
from collections import deque

class Queue:
    def __init__(self):
        self.buffer = deque()
        
    def enqueue(self, data):
        self.buffer.append(data)
        
    def dequeue(self):
        return self.buffer.popleft()

# Usage
my_queue = Queue()
my_queue.enqueue("User A")
my_queue.enqueue("User B")
print(f"Queue FIFO Dequeue: {my_queue.dequeue()}") # User A comes out first
