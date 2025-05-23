class stacksUsingPythonLists:
    def __init__(self):
        self.stack=[]

    def push(self,item):
        self.stack.append(item)
    def pop(self):
        if self.isEmpty():
            print("The stack is empty")
            return None
        else:
            return self.stack.pop()
    def peek(self):
        if self.isEmpty():
            print("The stack is empty")
            return None
        else:
            return self.stack[-1]
    def isEmpty(self):
        if len(self.stack)==0:
            return True
        else:
            return False

    def size(self):
        return len(self.stack)

stackOfNumbers=stacksUsingPythonLists()
stackOfNumbers.push(1)
stackOfNumbers.push(2)
stackOfNumbers.push(3)
stackOfNumbers.peek()
stackOfNumbers.isEmpty()
stackOfNumbers.pop()