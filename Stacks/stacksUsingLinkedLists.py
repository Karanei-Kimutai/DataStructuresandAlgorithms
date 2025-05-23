class Node:
    def __init__(self,data):
        self.data=data
        self.nextNode=None

class stacksUsingLinkedLists:
    def __init__(self):
        self.top=None  #This represents the top of the stack

    def push(self,item):
        newNode=Node(item)
        if self.top is None:
            self.top=newNode
        else:
            newNode.nextNode=self.top
            self.top=newNode

    def pop(self):
        if self.isEmpty():
            print("The stack is empty")
            return None
        else:
            poppedData=self.top.data
            self.top=self.top.nextNode
            return poppedData

    def isEmpty(self):
        if self.top is None:
            return True
        else:
            return False

    def size(self):
        count=0
        currentNode=self.top
        while currentNode is not None:
            count+=1
            currentNode=currentNode.nextNode
        return count


stack=stacksUsingLinkedLists()
stack.push(10)
stack.push(20)
stack.push(30)
print(stack.pop())
print(stack.size())