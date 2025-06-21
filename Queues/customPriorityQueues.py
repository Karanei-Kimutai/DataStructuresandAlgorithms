class customPriorityQueue:
    def __init__(self):
        self.items=[]  #List to store (priority,value) pairs

    def isEmpty(self):
        if len(self.items)==0:
            return True
        else:
            return False

    def insert(self,priority,value):
        pair=(priority,value)
        self.items.append(pair)

    def remove(self):
        if self.isEmpty():
            print("Priority queue is empty. Nothing to remove")
            return None

        #Find the item with the lowest priority number
        minimumIndex=0
        for index in range(1,len(self.items)):
            if self.items[index][0]<self.items[minimumIndex][0]:
                minimumIndex=index

        #Remove and return that item
        highestPriorityItem=self.items[minimumIndex]
        del self.items[minimumIndex]
        return highestPriorityItem

    def display(self):
        print("Priority Queue contents:")
        for priority,value in self.items:
            print(f"Value: {value}, Priority: {priority}")

priorityQueue=customPriorityQueue()
priorityQueue.insert(3,"C")
priorityQueue.insert(1,"A")
priorityQueue.insert(2,"B")

priorityQueue.display()

print("\nRemoving items by priority:")
while not priorityQueue.isEmpty():
    priority,value=priorityQueue.remove()
    print(f"Removed: {value} priority: {priority}")