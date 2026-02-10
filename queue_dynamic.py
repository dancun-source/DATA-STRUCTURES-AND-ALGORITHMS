# 4. LINEAR - DYNAMIC: Queue
# FIFO: First-In-First-Out
from collections import deque
queue = deque(["User1", "User2", "User3"])
print(f"Served: {queue.popleft()}") # Removes User1
