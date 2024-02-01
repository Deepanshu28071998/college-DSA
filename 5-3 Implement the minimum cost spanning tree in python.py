class Graph:
    def __init__(self,vertices):
        self.vertices=vertices
        self.edges=[]

    def add_edges(self, source, destination, weight):
        self.edges.append((source, destination, weight))
    def find_mst(self):
        mst=[]
        self.edges.sort(key=lambda x: x[2])
        visited = set()
        for edge in self.edges:
            source, destination, weight = edge
            if source not in visited:
                mst.append(edge)
                visited.add(source)
                # visited.add(destination)
        return mst
g=Graph(4)
g.add_edges(0, 1, 10)
g.add_edges(0, 2, 6)
g.add_edges(0, 3, 5)
g.add_edges(0, 3, 15)
g.add_edges(0, 3, 4) 
mst= g.find_mst()
print(mst)
