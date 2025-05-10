class Node:
    def __init__(self,data):
        self.data=data
        self.previousNode=None
        self.nextNode=None

class DoublyLinkedList:
    def __init__(self):
        self.headNode=None
    def insertAtEnd(self,value):
        newNode=Node(value)
        if self.headNode is None:
            self.headNode=newNode
            return
        else:
            currentNode=self.headNode
            while currentNode.nextNode is not None:
                currentNode=currentNode.nextNode
            currentNode.nextNode=newNode
            newNode.previousNode=currentNode
    def displayForward(self):
        if self.headNode is None:
            print("This list is empty")
        else:
            print("Forward traversal:")
            currentNode=self.headNode
            while currentNode is not None:
                print(currentNode.data, end="<->")
                currentNode=currentNode.nextNode
            print("None")
    def displayBackward(self):
        if self.headNode is None:
            print("This is an empty list")
            return
        else:
            lastNode=self.headNode
            while lastNode.nextNode is not None:
                lastNode=lastNode.nextNode
            print("Backward traversal:")
            currentNode=lastNode
            while currentNode is not None:
                print(currentNode.data, end="<->")
                currentNode=currentNode.previousNode
            print("None")


listOfNames=DoublyLinkedList()
listOfNames.insertAtEnd("Karanei")
listOfNames.insertAtEnd("Kimutai")
listOfNames.insertAtEnd("Michael")
listOfNames.displayForward()
listOfNames.displayBackward()
