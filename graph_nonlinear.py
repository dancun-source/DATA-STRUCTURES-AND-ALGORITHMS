# 6. NON-LINEAR (Graph)
# Classification: Non-Linear -> Graph
class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_edge(self, u, v):
        if u not in self.adj_list:
            self.adj_list[u] = []
        self.adj_list[u].append(v)

# Usage representing a Network
network = Graph()
network.add_edge("Router", "PC1")
network.add_edge("Router", "PC2")
network.add_edge("PC1", "Printer")

print("--- Non-Linear Data Structure (Graph) ---")
print(f"Network Connections: {network.adj_list}")
