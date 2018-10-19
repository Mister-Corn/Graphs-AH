"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, value):
        if value in self.vertices:
            raise Exception("Vertex already exists")
        else:
            self.vertices[value] = set() 

    def add_edge(self, vertex1, vertex2, bidirectional=True):
        if vertex1 not in self.vertices or vertex2 not in self.vertices:
            raise Exception("you cannot put an edge on nonexistent vertex")
        else:
            self.vertices[vertex1].add(vertex2)
            if bidirectional:
                self.vertices[vertex2].add(vertex1)
    def dfs(self, starting_node, visited=None):
        # Mark the node as visited
        if visited is None:
            # quese of visited nodes
            visited = []
        visited.append(starting_node)
        # For each child, if that child hasn't been visited, call dft() on that node
        for node in self.vertices[starting_node]:
            if node not in visited:
                self.dfs(node, visited)
        return visited
        # for child in children:
        #    if child not in visited:
        # dft(child, visted)

#graph = Graph()  # Instantiate your graph
#graph.add_vertex('0')
#graph.add_vertex('1')
#graph.add_vertex('2')
#graph.add_vertex('3')
#graph.add_edge('0', '1')
#graph.add_edge('0', '3')
#graph.add_edge('0', '4')
#print(graph.vertices)
