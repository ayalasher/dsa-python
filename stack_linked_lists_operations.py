print("What the title says")

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class stack:
    def __init__(self):
        self.head= None

    # A funtion to check if the stack is empty
    def isEmpty(self):
        return self.head is None
    
    # A funtion to push data to the stack
    def push(self,data):
        newNode = Node(data)

        # check if the stack is empty
        if self.isEmpty():
            self.head = newNode
        else:
            newNode.next = self.head
            self.head = newNode

    # A funtion to pop data from the stack 
    def pop(self):
        if self.isEmpty():
            print("The stack is Empty")
        else:
            poppeddata = self.head.data
            self.head = self.head.next
            return poppeddata
        
        # A funtion to peek data from the stack
    def peek(self):
        if self.isEmpty():
            print("The stack is empty")
        else:
            return self.head.data
            

stack = stack()

stack.push(3)
stack.push(4)
stack.push(5)
print(stack.peek())
