class generalTreeNode:
    def __init__(self,data):
        self.data=data
        self.children=[]

    def addChild(self,childNode):
        self.children.append(childNode)

    def removeChild(self,childNode):
       #Shorthand method: self.children=[child for child in self.children if child!=childNode]
       newChildren=[]
       for child in self.children:
           if child!=childNode:
               newChildren.append(child)
       self.children=newChildren

    def find(self,value):
        if self.data==value:
            return self
        for child in self.children:
            result=child.find(value)
            if result is not None:
                return result
        return None

    def printTree(self,level=0):
        print('    '*level+str(self.data))
        for child in self.children:
            child.printTree(level+1)


rootNode=generalTreeNode("Strathmore")
SCES=generalTreeNode("SCES")
SBS=generalTreeNode("SBS")
BICS=generalTreeNode("ICS")
BBIT=generalTreeNode("BBIT")
BCOM=generalTreeNode("BCOM")
Marketing=generalTreeNode("Marketing")
rootNode.addChild(SCES)
rootNode.addChild(SBS)
SCES.addChild(BBIT)
SCES.addChild(BICS)
SBS.addChild(BCOM)
SBS.addChild(Marketing)
rootNode.printTree()