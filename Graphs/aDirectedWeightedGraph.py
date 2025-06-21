class DirectedWeightedGraph:
    def __init__(self):
        self.adjacencyList={}  #  {vertex:[(neighbour,weight)]}

    def addVertex(self,vertex):
        if vertex not in self.adjacencyList:
            self.adjacencyList[vertex]=[]
        else:
            print(f"Vertex {vertex} already exists")

    def addEdge(self,fromVertex,toVertex,weight):
        if fromVertex not in self.adjacencyList:
            print(f"{fromVertex} does not exist")
            return
        if toVertex not in self.adjacencyList:
            print(f"{toVertex} does not exist")
            return

        self.adjacencyList[fromVertex].append((toVertex,weight))

    def removeEdge(self,fromVertex,toVertex):
        newNeighbours=[]
        for neighbourPair in self.adjacencyList[fromVertex]:
            neighbourVertex=neighbourPair[0]
            weight=neighbourPair[1]

            if neighbourVertex != toVertex:
                newNeighbours.append((neighbourVertex,weight))
        self.adjacencyList[fromVertex]=newNeighbours


    def printGraph(self):
        for vertex in self.adjacencyList:
            print(f"{vertex} --> {self.adjacencyList[vertex]}")


exampleGraph=DirectedWeightedGraph()
exampleGraph.addVertex("A")
exampleGraph.addVertex("B")
exampleGraph.addVertex("C")
exampleGraph.addVertex("D")

exampleGraph.addEdge("A","B",5)
exampleGraph.addEdge("A","C",2)
exampleGraph.addEdge("B","D",1)


exampleGraph.printGraph()