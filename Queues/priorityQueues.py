"""
 Priority queues are special types of queues where each element has a priority and elements with the highest priority are removed first
[(2, 'B'), (1, 'A'), (3, 'C')]->The lower the number the higher the priority eg A(priority 1) comes out first etc
Priority queues are used when we need to pick the best option first eg in Dijkstra's algorithm, A* Searches, Event scheduling systems, Task prioritization in operating systems
"""
import heapq

priorityQueue=[]
heapq.heappush(priorityQueue,(3,"C"))
heapq.heappush(priorityQueue,(1,"A"))
heapq.heappush(priorityQueue,(2,"B"))

while len(priorityQueue)>0:
    priority,value=heapq.heappop(priorityQueue)
    print("Popped: ",value," with priority: ", priority)

