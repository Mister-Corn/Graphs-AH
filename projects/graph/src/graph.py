"""
Simple graph implementation compatible with BokehGraph class.
"""
from collections import deque
import random

class Queue:
    def __init__(self):
        self.storage = deque()
        self.size = 0
    
    def enqueue(self, value):
        self.size += 1
        self.storage.append(value)
    
    def dequeue(self):
        if self.size > 0:
            self.size -= 1
            return self.storage.popleft()
        return None

    def get_size(self):
        return self.size

class Stack:
    def __init__(self):
        self.storage = deque()
        self.size = 0
    
    def push(self, value):
        self.size += 1
        self.storage.append(value)
    
    def pop(self):
        if self.size > 0:
            self.size -= 1
            return self.storage.pop()
        return None
    
    def get_size(self):
        return self.size

class Vertex:
    def __init__(self, value, X=None, Y=None):
        self.value = value # 0
        self.edges = set() # {'1', '3'}

        if X is None:
            self.x = random.random() * 10 - 5
        else:
            self.x = X  
        if Y is None:
            self.y = random.random() * 10 - 5
        else:
            self.y = Y

    def __repr__(self):
        return f"{self.edges}"
    
    def add_edge(self, vert_name):
        self.edges.add(vert_name)


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, value):
        if value in self.vertices:
            raise Exception("Vertex already exists")
        else:
            self.vertices[value] = Vertex(value) 

    def add_edge(self, vertex1, vertex2, bidirectional=True):
        if vertex1 not in self.vertices or vertex2 not in self.vertices:
            raise Exception("you cannot put an edge on nonexistent vertex")
        else:
            self.vertices[vertex1].add_edge(vertex2)
            if bidirectional:
                self.vertices[vertex2].add_edge(vertex1)

    def bfs(self, starting_node, target_value):
        """
        starting_node: string
        target_value: string

        """
        q = Queue()
        visited = []
        print('===starting node:', starting_node, 'target_value:', target_value)
        q.enqueue(starting_node)

        while q.get_size() > 0:
            current_vert = q.dequeue()
            print('===current_vert:', current_vert)
            if current_vert == target_value:
                return True
            visited.append(current_vert)
            for vert in self.vertices[current_vert].edges:
                if vert not in visited:
                    q.enqueue(vert)
        
        return False
    
    def dfs_stack(self, starting_node, target_value):
        s = Stack()
        visited = []

        s.push(starting_node)

        while s.get_size() > 0:
            current_vert = s.pop()
            print('===current_vert:', current_vert)
            if current_vert == target_value:
                return True
            visited.append(current_vert)
            for vert in self.vertices[current_vert].edges:
                if vert not in visited:
                    s.push(vert)
        
        return False

    def dfs(self, starting_node, target_value, visited=None):
        if visited == None:
            visited = []
        
        if starting_node == target_value:
            return True

        visited.append(starting_node)
        for vert in self.vertices[starting_node].edges:
            if vert not in visited:
                if self.dfs(vert, target_value, visited):
                    return True
                """
                Original proposal:
                `return self.dfs(vert, target_value, visited)`
                We need this return because in order to get an output from
                a function, we need to return it. Without a return, the value
                is generated, then essentially discarded.

                However, the problem is the return is in a middle of the loop.
                A return during an execution of a function immediately ends the
                function execution, and returns the value following it.

                A solution is to gate the return behind an if statement.
                """
        return False        
        

def main():
    graph = Graph()  # Instantiate your graph
    for n in range(6):
        graph.add_vertex(str(n))
    graph.add_edge('0', '1')
    graph.add_edge('0', '3')
    graph.add_edge('3', '4')
    print(graph.bfs('0', '5'))
    print(graph.dfs_stack('0', '5'))
    print(graph.dfs('0', '5'))

if __name__ == '__main__':
    main()