class Node:
    def __init__(self,data):
        self.data=data
        self.nextNode=None
        self.previousNode=None

class CircularDoublyLinkedList:
    def __init__(self):
        self.headNode=None
    def insertAtEnd(self,value):
        newNode=Node(value)
        if self.headNode is None:
            self.headNode=newNode
            newNode.nextNode=newNode
            newNode.previousNode=newNode
            return
        else:
            lastNode=self.headNode.previousNode
            lastNode.nextNode=newNode
            newNode.previousNode=lastNode
            newNode.nextNode=self.headNode
            self.headNode.previousNode=newNode
    def displayForward(self):
        if self.headNode is None:
            print("This list is empty")
            return
        else:
            print("Forward Traversal:")
            currentNode=self.headNode
            while True:
                print(currentNode.data,end="<->")
                currentNode=currentNode.nextNode
                if currentNode==self.headNode:
                    print("(back to head)")
                    break
    def displayBackward(self):
        if self.headNode is None:
            print("This list is empty")
            return
        else:
            currentNode=self.headNode.previousNode
            while True:
                print(currentNode.data,end="<->")
                currentNode=currentNode.previousNode
                if currentNode==self.headNode.previousNode:
                    print("(Back to tail)")
                    break

listOfNames=CircularDoublyLinkedList()
listOfNames.insertAtEnd("Karanei")
listOfNames.insertAtEnd("Kimutai")
listOfNames.insertAtEnd("Michael")
listOfNames.displayForward()
listOfNames.displayBackward()