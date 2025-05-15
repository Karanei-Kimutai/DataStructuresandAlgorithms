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

    def insertAtBeginning(self, value):
        newNode = Node(value)
        if self.headNode is None:
            self.headNode = newNode
        else:
            newNode.nextNode = self.headNode
            self.headNode.previousNode = newNode
            self.headNode = newNode

    def insertAtIndex(self,index,value):
        newNode=Node(value)
        if index==0:
            if self.headNode is None:
                self.headNode=newNode
                return
            else:
                newNode.nextNode=self.headNode
                self.headNode=newNode
        else:
            currentNode=self.headNode
            currentPosition=0
            while currentNode is not None and currentPosition<index-1:
                currentNode=currentNode.nextNode
                currentPosition+=1
            if currentNode is None:
                print("Index out of bounds")
            else:
                newNode.nextNode=currentNode.nextNode
                newNode.previousNode=currentNode
                if currentNode.nextNode is not None:
                    currentNode.nextNode.previousNode=newNode
                currentNode.nextNode=newNode

    def deleteFromBeginning(self):
        if self.headNode is None:
            print("This list is empty, nothing to delete")
            return
        if self.headNode.nextNode is None:
            self.headNode=None
        else:
            newHead=self.headNode.nextNode
            newHead.previousNode=None
            self.headNode.nextNode=None #Cleanup
            self.headNode=newHead

    def deleteFromEnd(self):
        if self.headNode is None:
            print("This list is empty, nothing to delete")
            return
        if self.headNode.nextNode is None:
            self.headNode=None
        else:
            currentNode=self.headNode
            while currentNode.nextNode is not None:
                currentNode=currentNode.nextNode
            currentNode.previousNode.nextNode=None
            currentNode.previousNode=None

    def deleteFromIndex(self,index):
        if self.headNode is None:
            print("The list is empty, nothing to delete")
            return
        if index==0:
            if self.headNode.nextNode is None:
                self.headNode=None
            else:
                newHeadNode=self.headNode.nextNode
                newHeadNode.previousNode=None
                self.headNode.nextNode=None #cleaning up
                self.headNode=newHeadNode
            return
        else:
            currentNode=self.headNode
            currentPosition=0
            while currentNode is not None and currentPosition<index-1:
                currentNode=currentNode.nextNode
                currentPosition+=1
            if currentNode is None or currentNode.nextNode is None:
                print("Index out of bounds")
                return
            else:
                nodeToDelete=currentNode.nextNode
                nodeAfterNodetoDelete=nodeToDelete.nextNode
                currentNode.nextNode=nodeAfterNodetoDelete
                if nodeAfterNodetoDelete is not None:
                    nodeAfterNodetoDelete.previousNode=currentNode
                nodeToDelete.nextNode=None #Cleanup
                nodeToDelete.previousNode=None #Cleanup



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

#Example
listOfNames=DoublyLinkedList()
listOfNames.insertAtEnd("Karanei")
listOfNames.insertAtEnd("Kimutai")
listOfNames.insertAtEnd("Michael")
listOfNames.insertAtBeginning("Bing Chilling")
listOfNames.insertAtIndex(2,"Maximus")
listOfNames.insertAtIndex(3,"Decimus")
listOfNames.deleteFromBeginning()
listOfNames.deleteFromEnd()
listOfNames.deleteFromIndex(1)
listOfNames.displayForward()
listOfNames.displayBackward()
