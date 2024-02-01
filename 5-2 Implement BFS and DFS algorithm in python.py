# Python program for Breadth First Search (BFS) algorithm

# A class to represent a graph
from collections import defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

	# A function used by DFS
    def DFS(self, v, visited):
        visited[v] = True
        print(v, end=' ')
        for neighbour in self.graph[v]:
            if visited[neighbour]==False:
                self.DFS(neighbour, visited)

	
    def printDFS(self, v):
        visited = {}
        for i in range(len(self.graph)):
            visited[i]=False
        self.DFS(v,visited)
    def BFS (self,v):
        visited={}
        for i in range(len(self.graph)):
            visited[i]=False
        queue=[]
        queue.append(v)
        visited[v]=True
        while queue:
            s=queue.pop(0)
            print(s,end=' ')
            for neighbour in self.graph[s]:
                if visited[neighbour]==False:
                    queue.append(neighbour)
                    visited[neighbour]=True
                        
                    

		

# Driver program
g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print("Following is Depth First Traversal")
g.printDFS(2)
print("\nBreadth First Traversal")
g.BFS(2)
