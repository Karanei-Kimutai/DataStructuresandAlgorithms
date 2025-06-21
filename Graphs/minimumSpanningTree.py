#Prim's algorithm is used to connect all nodes in a graph using the lowest total edge weight without cycles
import heapq

class minimumSpanningTreeGraph:
    def __init__(self):
        self.adjacencyList={}
    def addVertex(self,vertex):
        if vertex not in self.adjacencyList:
            self.adjacencyList[vertex]=[]

    def addEdge(self,vertex1,vertex2,edgeWeight):
        if vertex1 not in self.adjacencyList:
            self.addVertex(vertex1)
        if vertex2 not in self.adjacencyList:
            self.addVertex(vertex2)
        self.adjacencyList[vertex1].append((vertex2,edgeWeight))
        self.adjacencyList[vertex2].append((vertex1,edgeWeight))

    def calculatePrimMinimumSpanningTreeCost(self,startingVertex):
        visitedVertices=set()
        minimumEdgeHeap=[]
        totalMinimumCost=0

        #start by pushing (0,startingVertex)
        initialEntry=(0,startingVertex)
        heapq.heappush(minimumEdgeHeap,initialEntry)

        while len(minimumEdgeHeap)>0:
            edgeWeight,currentVertex=heapq.heappop(minimumEdgeHeap)

            if currentVertex in visitedVertices:
                continue
            visitedVertices.add(currentVertex)
            totalMinimumCost+=edgeWeight

            neighboursList=self.adjacencyList[currentVertex]
            for neighbourVertex,neighbourEdgeweight in neighboursList:
                if neighbourVertex not in visitedVertices:
                    nextEntry=(neighbourEdgeweight,neighbourVertex)
                    heapq.heappush(minimumEdgeHeap,nextEntry)

        return totalMinimumCost


graph = minimumSpanningTreeGraph()

graph.addVertex("A")
graph.addVertex("B")
graph.addVertex("C")
graph.addVertex("D")

graph.addEdge("A", "B", 3)
graph.addEdge("A", "C", 1)
graph.addEdge("B", "C", 7)
graph.addEdge("B", "D", 5)
graph.addEdge("C", "D", 2)

cost = graph.calculatePrimMinimumSpanningTreeCost("A")
print("Total cost of MST:", cost)
