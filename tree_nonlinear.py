# 5. NON-LINEAR (Tree)
# Classification: Non-Linear -> Tree
class TreeNode:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

# Creating a hierarchical structure
root = TreeNode("CEO")
root.left = TreeNode("Manager A")
root.right = TreeNode("Manager B")

print("--- Non-Linear Data Structure (Tree) ---")
print(f"Root: {root.val} | Left Child: {root.left.val} | Right Child: {root.right.val}")
