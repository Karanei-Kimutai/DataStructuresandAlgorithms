class directedAcyclicGraph:
    def __init__(self):
        self.adjacencyList={}

    def addVertex(self,vertex):
        if vertex not in self.adjacencyList:
            self.adjacencyList[vertex]=[]

    def addEdge(self,fromVertex,toVertex):
        if fromVertex not in self.adjacencyList:
            self.addVertex(fromVertex)
        if toVertex not in self.adjacencyList:
            self.addVertex(toVertex)
        self.adjacencyList[fromVertex].append(toVertex)

    def getTopologicalSort(self):
        visitedVertices=set()
        topologicalOrder=[]
        def depthFirstSearch(vertex):
            visitedVertices.add(vertex)
            for neighbour in self.adjacencyList[vertex]:
                if neighbour not in visitedVertices:
                    depthFirstSearch(neighbour)
            topologicalOrder.append(vertex)
        for vertex in self.adjacencyList:
            if vertex not in visitedVertices:
                depthFirstSearch(vertex)
        #Reverse the order manually
        sortedOrder=[]
        index=len(topologicalOrder)-1
        while index>=0:
            sortedOrder.append(topologicalOrder[index])
            index-=1
        return sortedOrder

exampleGraph = directedAcyclicGraph()
exampleGraph.addVertex("Cook")
exampleGraph.addVertex("Eat")
exampleGraph.addVertex("Buy Groceries")
exampleGraph.addVertex("Wash Hands")

exampleGraph.addEdge("Buy Groceries", "Cook")
exampleGraph.addEdge("Cook", "Wash Hands")
exampleGraph.addEdge("Wash Hands", "Eat")

print("Topological Order:")
order = exampleGraph.getTopologicalSort()
for task in order:
    print(task)