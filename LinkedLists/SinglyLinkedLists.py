class Node:
    def __init__(self,data):
        self.data=data
        self.nextNode=None

class singlyLinkedList:
    def __init__(self):
        self.headNode=None
    def insertAtEnd(self,value):
        newNode=Node(value)
        if self.headNode is None:
            self.headNode=newNode
        else:
            currentNode=self.headNode
            while currentNode.nextNode is not None:
                currentNode=currentNode.nextNode
            currentNode.nextNode=newNode

    def insertAtBeginning(self,value):
        newNode=Node(value)
        if self.headNode is None:
            self.headNode=newNode
        else:
            newNode.nextNode=self.headNode
            self.headNode=newNode

    def insertAtIndex(self,index,value):
        newNode=Node(value)
        if index==0:
            newNode.nextNode=self.headNode
            self.headNode=newNode
            return
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
                currentNode.nextNode=newNode

    def deleteFromBeginning(self):
        if self.headNode is None:
            print("This list is empty, nothing to delete.")
        else:
            self.headNode=self.headNode.nextNode

    def deleteFromEnd(self):
        if self.headNode is None:
            print("This list is empty, nothing to delete")
        elif self.headNode.nextNode is None:
            self.headNode=None
        else:
            currentNode=self.headNode
            while currentNode.nextNode.nextNode is not None:
                currentNode=currentNode.nextNode
            currentNode.nextNode=None

    def deleteFromIndex(self,index):
        if self.headNode is None:
            print("The list is empty, nothing to delete.")
        elif index==0:
            self.headNode=self.headNode.nextNode
        else:
            currentNode=self.headNode
            currentPosition=0
            while currentNode is not None and currentPosition<index-1:
                currentNode=currentNode.nextNode
                currentPosition+=1
            if currentNode is None or currentNode.nextNode is None:
                print("Index out of bounds")
            else:
                currentNode.nextNode=currentNode.nextNode.nextNode


    def showListItems(self):
        currentNode=self.headNode
        while currentNode is not None:
            print(currentNode.data, end="->")
            currentNode=currentNode.nextNode
        print("None")


#Examples
listOfNames=singlyLinkedList()
listOfNames.insertAtEnd("Karanei")
listOfNames.insertAtEnd("Kimutai")
listOfNames.insertAtEnd("Michael")
listOfNames.showListItems()

listOfNames.insertAtBeginning("Bing Chilling")
listOfNames.showListItems()
listOfNumbers=singlyLinkedList()
listOfNumbers.insertAtEnd(1)
listOfNumbers.insertAtEnd(2)
listOfNumbers.insertAtEnd(3)
listOfNumbers.showListItems()

listOfNames.deleteFromEnd()
listOfNames.showListItems()
listOfNumbers.deleteFromBeginning()
listOfNumbers.showListItems()
listOfNames.insertAtIndex(0,"Kimutai")
listOfNames.showListItems()
listOfNumbers.deleteFromIndex(0)
listOfNumbers.showListItems()