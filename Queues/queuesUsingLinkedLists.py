class Node:
    def __init__(self,data):
        self.data=data
        self.nextNode=None

class queueUsingLinkedList:
    def __init__(self):
        self.front=None
        self.rear=None

    def enqueue(self,item):
        newNode=Node(item)
        if self.rear is None:
            self.front=self.rear=newNode
        else:
            self.rear.nextNode=newNode
            self.rear=newNode

    def dequeue(self):
        if self.isEmpty():
            print("The queue is empty")
            return None
        else:
            value=self.front.data
            self.front=self.front.nextNode
            if self.front is None:  #Case where there was only one item in the queue
                self.rear=None
            return value

    def peek(self):
        if self.isEmpty():
           print("The queue is empty")
           return None
        else:
            return self.front.data

    def isEmpty(self):
        if self.front is None:
            return True
        else:
            return False

    def size(self):
        count=0
        currentNode=self.front
        while currentNode is not None:
            count+=1
            currentNode=currentNode.nextNode
        return count


queueUsingLinkedListExample=queueUsingLinkedList()
queueUsingLinkedListExample.enqueue(10)
queueUsingLinkedListExample.enqueue(20)
queueUsingLinkedListExample.enqueue(30)
print(queueUsingLinkedListExample.dequeue())
print(queueUsingLinkedListExample.peek())
print(queueUsingLinkedListExample.size())