class circularQueue:
    def __init__(self,capacity):
        if isinstance(capacity,int) is False or capacity<=0:
            raise ValueError("Capacity must be a positive integer.")
        self.capacity=capacity
        self.queue=[None]*capacity #Creates a list where each element is None. Also, self.queue=[None]*3 is the same as saying self.queue=[None,None,None]
        self.front=0  #index of the front element
        self.rear=0   #index where the next element will be added
        self.count=0  #current number of elements in the queue

    def enqueue(self,item):
        if self.isFull():
            print("Queue is full, cannot enqueue")
            return False
        else:
            self.queue[self.rear]=item
            self.rear=(self.rear+1)%self.capacity
            self.count+=1

    def dequeue(self):
        if self.isEmpty():
            print("The queue is empty")
            return None
        else:
            value=self.queue[self.front]
            self.queue[self.front]=None
            self.front=(self.front+1)%self.capacity
            self.count-=1
            return value

    def peek(self):
        if self.isEmpty():
            print("The queue is empty")
            return None
        else:
            return self.queue[self.front]

    def isEmpty(self):
        if self.count==0:
            return True
        else:
            return False

    def isFull(self):
        if self.count==self.capacity:
            return True
        else:
            return False

    def display(self):
        if self.isEmpty():
            print("The queue is empty")
        else:
            index=self.front
            items=[]
            for i in range(self.count):
                items.append(self.queue[index])
                index=(index+1)%self.capacity
            print("Queue contents:", items)


circularQueueExample=circularQueue(5)
circularQueueExample.enqueue(10)
circularQueueExample.enqueue(20)
circularQueueExample.enqueue(30)
circularQueueExample.enqueue(40)
circularQueueExample.enqueue(50)
circularQueueExample.display()
circularQueueExample.dequeue()
circularQueueExample.dequeue()
circularQueueExample.enqueue(60)
circularQueueExample.enqueue(70)
circularQueueExample.display()
print(circularQueueExample.peek())
