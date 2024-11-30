class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class queue:
    def __init__(self) :
        self.front = None
        self.rear = None

        # Checking if the queue ie empty
    def isEmpty(self):
        return self.front is None
    
    # Display contents of the queue
    def display(self):
        if self.isEmpty():
            print("The queue is empty")
        else :
            current = self.front
            while current:
               print(current.data) 
               current = current.next
    # Add items at the back of the queue
    def enqueue(self,data):
        newNode = Node(data)
        # Check if the rear is none
        if self.rear is None:
            self.front = newNode
            self.rear = newNode
        else:
            self.rear.next = newNode
            self.rear = newNode

    def dequeue(self):
        if self.isEmpty():
            print("The queue is empty")
            return
        else:
            self.front = self.front.next 
            if self.front is None:
               self.rear = None
            return
    def peek(self):
        if self.isEmpty():
            print("The stack is empty")
        else:
            return self.front.data

    



# Creating the queue
fruits = queue()

# Adding items to the queue
fruits.enqueue("apple")
fruits.enqueue("banana")
fruits.enqueue("watermelon")
fruits.enqueue("Kiwi")

# Removing items from the queue from the top
fruits.dequeue()

#Peeking

print(f"The item at the peek is : {fruits.peek()}")


# Print elements of the queue
fruits.display()