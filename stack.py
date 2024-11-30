class stack:
    def __init__(self) :
        self.list =[]

        # Checking if the list is empty
    def isempty(self):
        return self.list == []
    

    # Adding elements on top of the stack...
    def push(self , value):
        self.list.append(value)

    #removing an element from the top of the stack
    def pop(self):
        if self.isempty():
            raise Exception("The list is empty")
        return self.list.pop()
    

    # Checking element on top of the stack
    def peek(self):
        if self.isempty():
            raise Exception("The list is empty")
        print(self.list[-1]) #This will return the last / top most element in the list
    


mystack = stack()




mystack.push(1)
mystack.push(2)
mystack.push(3)
mystack.push(4)

# Peeking
mystack.peek()