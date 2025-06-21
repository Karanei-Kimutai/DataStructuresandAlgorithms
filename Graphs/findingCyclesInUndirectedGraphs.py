class UndirectedGraph:
    def __init__(self):
        self.adjacencyList={}

    def addVertex(self,vertex):
        if vertex not in self.adjacencyList:
            self.adjacencyList[vertex]=[]

    def addEdge(self,vertex1,vertex2):
        if vertex1 not in self.adjacencyList:
            self.addVertex(vertex1)
        if vertex2 not in self.adjacencyList:
            self.addVertex(vertex2)
        self.adjacencyList[vertex1].append(vertex2)
        self.adjacencyList[vertex2].append(vertex1)

    def hasCycle(self):#returns True if the graph contains at least one cycle
        visitedVertices=set()
        def depthFirstSearch(currentVertex,parentVartex):
            visitedVertices.add(currentVertex)
            neighbourList=self.adjacencyList[currentVertex]
            for neighbour in neighbourList:
                if neighbour not in visitedVertices:
                    if depthFirstSearch(neighbour,currentVertex):
                        return True
                elif neighbour !=parentVartex:
                    return True

            return False

        for vertex in self.adjacencyList:
            if vertex not in visitedVertices:
                if depthFirstSearch(vertex,None):
                    return True

        return False


example=UndirectedGraph()
for vertex in ["A","B","C","D"]:
    example.addVertex(vertex)
example.addEdge("A","B")
example.addEdge("B","C")
example.addEdge("C","A")

if example.hasCycle():
    print("Cycle found")



