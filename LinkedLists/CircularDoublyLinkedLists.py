class Node:
    def __init__(self,data):
        self.data=data
        self.nextNode=None
        self.previousNode=None

class CircularDoublyLinkedList:
    def __init__(self):
        self.headNode=None

    def insertAtBeginning(self,value):
        newNode=Node(value)
        if self.headNode is None:
            self.headNode=newNode
            newNode.nextNode=newNode
            newNode.previousNode=newNode
            return
        else:
            tailNode=self.headNode.previousNode
            newNode.nextNode=self.headNode
            newNode.previousNode=tailNode
            self.headNode.previousNode=newNode
            tailNode.nextNode=newNode
            self.headNode=newNode
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

    def insertAtIndex(self,index,value):
        newNode=Node(value)
        if index==0:
            self.insertAtBeginning(value)
            return
        else:
            currentNode=self.headNode
            currentPosition=0
            while currentNode.nextNode!=self.headNode and currentPosition< index-1:
                currentNode=currentNode.nextNode
                currentPosition+=1
            if currentPosition!=index-1:
                print("Index out of bounds")
            else:
                newNode.nextNode=currentNode.nextNode
                newNode.previousNode=currentNode
                currentNode.nextNode.previousNode=newNode
                currentNode.nextNode=newNode

    def deleteFromBeginning(self):
        if self.headNode is None:
            print("List is empty, nothing to delete")
            return
        if self.headNode.nextNode==self.headNode:
            self.headNode=None
            return
        else:
            tailNode=self.headNode.previousNode
            newHead=self.headNode.nextNode
            tailNode.nextNode=newHead
            newHead.previousNode=tailNode
            self.headNode.nextNode=None #Cleanup
            self.headNode.previousNode=None #Cleanup
            self.headNode=newHead

    def deleteFromEnd(self):
        if self.headNode is None:
            print("List is empty, nothing to delete")
            return
        if self.headNode.nextNode==self.headNode:
            self.headNode=None
            return
        else:
            tailNode=self.headNode.previousNode
            newTail=tailNode.previousNode
            newTail.nextNode=self.headNode
            self.headNode.previousNode=newTail
            tailNode.nextNode=None #Cleanup
            tailNode.previousNode=None #Cleanup

    def deleteFromIndex(self,index):
        if self.headNode is None:
            print("List is empty, nothing to delete")
            return
        if index==0:
            self.deleteFromBeginning()
            return
        else:
            currentNode=self.headNode
            currentPosition=0
            while currentNode.nextNode!=self.headNode and currentPosition<index-1:
                currentNode=currentNode.nextNode
                currentPosition+=1
            if currentNode.nextNode==self.headNode or currentPosition!=-1:
                print("Index out of bounds")
                return
            else:
                nodeToDelete=currentNode.nextNode
                nodeAfterNodeToDelete=nodeToDelete.nextNode
                currentNode.nextNode=nodeAfterNodeToDelete
                nodeAfterNodeToDelete.previousNode=currentNode
                nodeToDelete.nextNode=None
                nodeToDelete.previousNode=None

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
listOfNames.insertAtBeginning("Bing Chilling")
listOfNames.insertAtIndex(2,"Maximus")
listOfNames.insertAtIndex(3,"Decimus")
listOfNames.deleteFromBeginning()
listOfNames.deleteFromEnd()
listOfNames.deleteFromIndex(1)
listOfNames.displayForward()
listOfNames.displayBackward()