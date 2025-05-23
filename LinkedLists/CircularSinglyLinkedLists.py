#Circular singly linked list
from operator import index


class Node:
    def __init__(self,data):
        self.data=data
        self.nextNode=None
class circularSinglyLinkedList:
    def __init__(self):
        self.headNode=None

    def insertAtBeginning(self,value):
        newNode=Node(value)
        if self.headNode is None:
            self.headNode=newNode
            newNode.nextNode=newNode
            return
        else:
            currentNode=self.headNode
            while currentNode.nextNode!=self.headNode:
                currentNode=currentNode.nextNode
            newNode.nextNode=self.headNode
            currentNode.nextNode=newNode
            self.headNode=newNode

    def insertAtEnd(self,value):
        newNode=Node(value)
        if self.headNode is None:
            self.headNode=newNode
            newNode.nextNode=newNode
            return
        else:
            currentNode=self.headNode
            while currentNode.nextNode!=self.headNode:
                currentNode=currentNode.nextNode
            currentNode.nextNode=newNode
            newNode.nextNode=self.headNode

    def insertAtIndex(self,index,value):
        newNode=Node(value)
        if index==0:
            self.insertAtBeginning(value)
            return
        else:
            currentNode=self.headNode
            currentPosition=0
            while currentNode.nextNode!=self.headNode and currentPosition<index-1:
                currentNode=currentNode.nextNode
                currentPosition+=1
            if currentPosition !=index-1:
                print("Index out of bounds")
            else:
                newNode.nextNode=currentNode.nextNode
                currentNode.nextNode=newNode

    def deleteFromBeginning(self):
        if self.headNode is None:
            print("List is empty, nothing to delete")
            return
        if self.headNode.nextNode==self.headNode:
            self.headNode=None
            return
        else:
            currentNode=self.headNode
            while currentNode.nextNode!=self.headNode:
                currentNode=currentNode.nextNode
            currentNode.nextNode=self.headNode.nextNode
            self.headNode=self.headNode.nextNode

    def deleteFromEnd(self):
        if self.headNode is None:
            print("List is empty, nothing to delete")
            return
        if self.headNode.nextNode==self.headNode:
            self.headNode=None
            return
        else:
            currentNode=self.headNode
            while currentNode.nextNode.nextNode!=self.headNode:
                currentNode=currentNode.nextNode
            currentNode.nextNode=self.headNode

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
            while currentNode.nextNode!=self.headNode and currentPosition< index-1:
                currentNode=currentNode.nextNode
                currentPosition+=1
            if currentNode.nextNode==self.headNode or currentPosition!=index-1:
                print("Index out of bounds")
                return
            else:
                nodeToDelete=currentNode.nextNode
                currentNode.nextNode=nodeToDelete.nextNode
                nodeToDelete.nextNode=None #cleanup

    def deleteByValue(self,value):
        if self.headNode is None:
            print("This list is empty, nothing to delete")
            return
        else:
            currentNode=self.headNode
            previousNode=None
            while True:
                if currentNode.data==value:
                    if currentNode==self.headNode:
                        if currentNode.nextNode==self.headNode:
                            self.headNode=None
                        else:
                            temp=self.headNode
                            while temp.nextNode!=self.headNode:
                                temp=temp.nextNode
                            temp.nextNode=currentNode.nextNode
                            self.headNode=currentNode.nextNode
                    else:
                        previousNode.nextNode=currentNode.nextNode
                    return
                else:
                    previousNode=currentNode
                    currentNode=currentNode.nextNode
                if currentNode==self.headNode:
                    break
        print("Value not found in the list")



    def display(self):
        if self.headNode is None:
            print("Empty List")
            return
        else:
            currentNode=self.headNode
            while True:
                print(currentNode.data,end="->")
                currentNode=currentNode.nextNode
                if currentNode==self.headNode:
                    print("(back to head)")
                    break

listOfNames=circularSinglyLinkedList()
listOfNames.insertAtEnd("Karanei")
listOfNames.insertAtEnd("Kimutai")
listOfNames.insertAtEnd("Michael")
listOfNames.insertAtBeginning("Bing Chilling")
listOfNames.insertAtIndex(2,"Maximus")
listOfNames.insertAtIndex(3,"Decimus")
listOfNames.deleteFromBeginning()
listOfNames.deleteFromEnd()
listOfNames.deleteFromIndex(1)
listOfNames.deleteByValue("Maximus")
listOfNames.display()



