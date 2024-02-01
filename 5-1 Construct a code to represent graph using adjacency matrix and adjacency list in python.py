'''
class Graph:
  def __init__(self, vertices):
    self.V = vertices
    self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

  def addEdge(self, u, v, w):
    self.graph[u][v] = w

  def printGraph(self):
    for i in range(self.V):
      for j in range(self.V):
        if self.graph[i][j] > 0:
          print(self.graph[i][j], end=" ")
      print()

# Driver program
g = Graph(4)
g.addEdge(0, 1, 10)
g.addEdge(0, 2, 6)
g.addEdge(0, 3, 5)
g.addEdge(1, 3, 15)
g.addEdge(2, 3, 4)

print("Following is the adjacency matrix")
g.printGraph()
'''

from collections import defaultdict

class graph:
  def _init_(self, V):
    self.V = V
    self.adjMatrix = [[0 for i in range(V)] for j in range(V)]
    self.adjList = [[]for i in range(V)]

  def addEdge(self, u, v):
    self.adjMatrix[u][v] = 1
    
    self.adjList[u].append(v)
    self.adjMatrix[v][u] = 1
    self.adjList[v].append(u)

  def printAdjMatrix(self):
    for i in self.adjMatrix:
      print(i)
      #for j in range(self.V):
       # print(self.adjMatrix[i][j], end = " ")
    #print()

  def printAdjList(self):
    for j in self.adjList:
      print(f"{i}:{adjList}")
    #print()

# Driver program
g = graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 3)

print("Adjacency Matrix")
g.printAdjMatrix()

print("Adjacency List")
g.printAdjList()

