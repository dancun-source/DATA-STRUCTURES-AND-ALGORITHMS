# 2. LINEAR - DYNAMIC (Linked List)
# Classification: Linear -> Dynamic
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Implementation
head = Node("First Item")
second = Node("Second Item")
head.next = second # Linking nodes dynamically in memory

print("--- Dynamic Data Structure (Linked List) ---")
print(f"Head: {head.data} -> Next: {head.next.data}")
