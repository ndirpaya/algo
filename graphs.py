class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    # Get the keys of the dictionary
    def getVertices(self):
        return list(self.gdict.keys())

    def edges(self):
        return self.findEdges()

    # Find the distinct list of edges
    def findEdges(self):
        edgename = []
        for vertex in self.gdict:
            for next_vertex in self.gdict[vertex]:
                if {next_vertex, vertex} not in edgename:
                    edgename.append({vertex, next_vertex})
        return edgename

    # Add the vertex as a key
    def addVertex(self, vertex):
        if vertex not in self.gdict:
            self.gdict[vertex] = []

    # Add new edge
    def addEdge(self, edge):
        edge = set(edge)
        (vertex1, vertex2) = tuple(edge)
        if vertex1 in self.gdict:
            self.gdict[vertex1].append(vertex2)
        else:
            self.gdict[vertex1] = vertex2
    

# Create the dictionary with graph elements
graph_elements = {
    "a" : ["b", "c"],
    "b" : ["a", "c"],
    "c" : ["a", "d"],
    "d" : ["c", "d"],
    "e" : ["d", "e"]
}

g = Graph(graph_elements)
# print(g.getVertices())
# print(g.edges())
# g.addVertex("f")
# print(g.getVertices())
g.addEdge({'a', 'e'})
# g.addEdge({'a', 'f'})
print(g.findEdges())