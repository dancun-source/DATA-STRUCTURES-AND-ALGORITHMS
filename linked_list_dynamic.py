# 2. LINEAR - DYNAMIC: Linked List
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

head = Node("First Node")
head.next = Node("Second Node")
