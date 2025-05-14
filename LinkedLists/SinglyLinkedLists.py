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

    def showListItems(self):
        currentNode=self.headNode
        while currentNode is not None:
            print(currentNode.data, end="->")
            currentNode=currentNode.nextNode
        print("None")

listOfNames=singlyLinkedList()
listOfNames.insertAtEnd("Karanei")
listOfNames.insertAtEnd("Kimutai")
listOfNames.insertAtEnd("Michael")
listOfNames.showListItems()

listOfNumbers=singlyLinkedList()
listOfNumbers.insertAtEnd(1)
listOfNumbers.insertAtEnd(2)
listOfNumbers.insertAtEnd(3)
listOfNumbers.showListItems()