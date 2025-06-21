class Graph:
    def __init__(self):
        self.adjacencyList={}  #Stores the graph using a dictionary: {node: [neighbours]}

    def addVertex(self,vertex):
         if vertex not in self.adjacencyList:
            self.adjacencyList[vertex]=[]
         else:
            print(f"Vertex {vertex} already exists")

    def addEdge(self, vertex1, vertex2):
        if vertex1 not in self.adjacencyList:
            print(f"{vertex1} does not exist.")
            return
        if vertex2 not in self.adjacencyList:
            print(f"{vertex2} does not exist")
            return
        if vertex2 not in self.adjacencyList[vertex1]:
            self.adjacencyList[vertex1].append(vertex2)
        if vertex1 not in self.adjacencyList[vertex2]:
            self.adjacencyList[vertex2].append(vertex1)

    def printGraph(self):
        for vertex in self.adjacencyList:
            print(f"{vertex}-->{self.adjacencyList[vertex]}")

    def breadthFirstSearch(self,start):
        visited=set()
        queue=[start]

        while len(queue)>0: #Can also be written as while queue
            vertex=queue.pop(0)
            if vertex not in visited:
                print(vertex,end=" ")
                visited.add(vertex)
                for neighbour in self.adjacencyList[vertex]:
                    if neighbour not in visited:
                        queue.append(neighbour)

    def depthFirstSearch(self,startingVertex):
        visitedVertices=set()
        self._exploreDepthFirst(startingVertex,visitedVertices)

    def _exploreDepthFirst(self,currentVertex,visitedVertices):
        if currentVertex not in visitedVertices:
          print(currentVertex, end=" ")
          visitedVertices.add(currentVertex)

          for neighbourVertex in self.adjacencyList[currentVertex]:
              self._exploreDepthFirst(neighbourVertex,visitedVertices)


undirectedUnweightedGraph=Graph()
undirectedUnweightedGraph.addVertex("A")
undirectedUnweightedGraph.addVertex("B")
undirectedUnweightedGraph.addVertex("C")
undirectedUnweightedGraph.addVertex("D")

undirectedUnweightedGraph.addEdge("A","B")
undirectedUnweightedGraph.addEdge("A","C")
undirectedUnweightedGraph.addEdge("B","D")
undirectedUnweightedGraph.addEdge("C","D")

undirectedUnweightedGraph.printGraph()

print("Breadth first search from A:")
undirectedUnweightedGraph.breadthFirstSearch("A")

print("\nDepth first search from A:")
undirectedUnweightedGraph.depthFirstSearch("A")