#graphs.py
from collections import defaultdict

class Graph:
    def __init__(self):
        self.nodes = defaultdict(list)
    
    def add_edge(self, u, v):
        self.nodes[u].append(v)
    
    def BFS(self, start, search_val):
        # breadth first search
        visited = set([start])
        queue = [start]
        while queue:
            current_node = queue.pop(0)
            print(current_node, "->")
            if current_node == search_val:
                return True
            else:
                for neighbor in self.nodes[current_node]:
                    if neighbor not in visited:
                        queue.append(neighbor)
                        visited.add(neighbor)
        return False
    
    def DFS(self, start, search_val, visited = None):
        # depth first search
        visited = visited or set()
    
        print(start, "->")
        if start == search_val:
            return True
        else:
            visited.add(start)
            for neighbour in self.nodes[start]:
                if neighbour not in visited:
                    if self.DFS(neighbour, search_val, visited):
                        return True
        return False
    
if __name__ == "__main__":
    # Test the graph class
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)
    g.add_edge(4, 5)
    g.add_edge(3, 6)
    
    print("BFS:")
    print(g.BFS(0, 6))
    print(g.BFS(0, -1))
    
    
    print("DFS:")
    print(g.DFS(0, 6))
    print(g.DFS(0, -1))
                

