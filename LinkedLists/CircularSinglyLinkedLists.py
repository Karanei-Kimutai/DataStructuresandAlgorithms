#Circular singly linked list
class Node:
    def __init__(self,data):
        self.data=data
        self.nextNode=None
class circularSinglyLinkedList:
    def __init__(self):
        self.headNode=None
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

listofNames=circularSinglyLinkedList()
listofNames.insertAtEnd("Karanei")
listofNames.insertAtEnd("Kimutai")
listofNames.insertAtEnd("Michael")

listofNames.display()



#circular doubly linked list
