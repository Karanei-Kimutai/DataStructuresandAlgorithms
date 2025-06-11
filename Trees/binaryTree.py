class binaryTreeNode:
    def __init__(self,data):
        self.data=data
        self.leftChildNode=None
        self.rightChildNode=None

    def insertLeft(self,childData):
        if self.leftChildNode is not None:
            raise Exception(f"Left child already exists for node {self.data}")
        else:
            self.leftChildNode=binaryTreeNode(childData)

    def insertRight(self,childData):
        if self.rightChildNode is not None:
            raise Exception(f"Right child already exists for node {self.data}")
        else:
            self.rightChildNode=binaryTreeNode(childData)

    def preOrderTraversal(self):
        #The root node is visited first, then the left subtree and finally the right subtree
        result=[self.data]
        if self.leftChildNode is not None:
            result+=self.leftChildNode.preOrderTraversal()
        if self.rightChildNode is not None:
            result+=self.rightChildNode.preOrderTraversal()
        return result

    def inOrderTraversal(self):
        #The left subtree is visited first, then the root node, then the right subtree
        result=[]
        if self.leftChildNode is not None:
            result+=self.leftChildNode.inOrderTraversal()
        result.append(self.data)
        if self.rightChildNode is not None:
            result+=self.rightChildNode.inOrderTraversal()
        return result

    def postOrderTraversal(self):
        #The left subtree is visited first, then the right subtree, then the root node
        result=[]
        if self.leftChildNode is not None:
            result+=self.leftChildNode.postOrderTraversal()
        if self.rightChildNode is not None:
            result+=self.rightChildNode.postOrderTraversal()
        result.append(self.data)
        return result

    def height(self):
        if self.leftChildNode is not None:
            leftHeight=self.leftChildNode.height()
        else:
            leftHeight=0

        if self.rightChildNode is not None:
            rightHeight=self.rightChildNode.height()
        else:
            rightHeight=0
        return 1+max(leftHeight,rightHeight)

rootNode=binaryTreeNode("A")
rootNode.insertLeft("B")
rootNode.insertRight("C")
try:
    rootNode.insertRight("D")
except Exception as e:
    print("Error: ",e)
try:
    rootNode.leftChildNode.insertLeft("D")
except TypeError as e:
    print("Error: the node onto which you want to add another node does not exist")
try:
    rootNode.leftChildNode.insertRight("E")
except TypeError as e:
    print("Error: the node onto which you want to add another node does not exist")
try:
    rootNode.rightChildNode.insertLeft("G")
except TypeError as e:
    print("Error: the node onto which you want to add another node does not exist")
try:
    rootNode.rightChildNode.insertRight("H")
except TypeError as e:
    print("Error: the node onto which you want to add another node does not exist")

print("Inorder:",rootNode.inOrderTraversal())
print("Preorder:",rootNode.preOrderTraversal())
print("Postorder:",rootNode.postOrderTraversal())
print("Height:",rootNode.height())