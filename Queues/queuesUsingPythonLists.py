class queueUsingList:
    def __init__(self):
        self.queue=[]

    def enqueue(self,item):
        self.queue.append(item)

    def dequeue(self):
        if self.isEmpty():
            print("The queue is empty")
        else:
            return self.queue.pop(0)

    def peek(self):
        if self.isEmpty():
            print("The queue is empty")
            return None
        else:
            return self.queue[0]

    def isEmpty(self):
        if len(self.queue)==0:
            return True
        else:
            return False

    def size(self):
        return len(self.queue)


queueExample=queueUsingList()
queueExample.enqueue(10)
queueExample.enqueue(20)
queueExample.enqueue(30)
print(queueExample.dequeue())
print(queueExample.peek())
print(queueExample.isEmpty())
print(queueExample.size())



