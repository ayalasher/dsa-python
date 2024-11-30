print("Working with linked lists")
# A linked  list has the head , the node and the end.... train format


# creating the node class
class Node:
    # Initilisation funtion(a constructor function)
    def __init__(self,data):
        self.data = data
        self.next = None


# Creating a linked list class to implement a linked list operation 
class Singlylinkedlist:
    # Initialization funtion
    # Creating the head of the linked list
    def __init__(self,):
        self.head = None


    def insertatbeginning(self,data):
        # Creating the node
        newnode = Node(data)
        # Check if the hea d is empty
        if self.head is None:
            self.head = newnode
        else:
            # Point the newnode to the head
            newnode.next = self.head
            self.head = newnode

    # Funtion to add node to the end of the linked list..
    def insertatend(self, data):
        Newnode = Node(data)
        # Check if the head is none
        if self.head is None:
            # Point the head to this new node..
            self.head = Newnode
        else:
            # Traverse he linked list to the last node....
            last = self.head
            while last.next :
                last = last.next
            last.next = Newnode

    # Function to delete a node
    def deleteinbetween(self, value):
        # Check if the linked list is empty
        if self.head is None:
            print("The linked list is empty")
            return
        
        # Deleting the head node
        if self.head.data == value:
            current = self.head
            self.head = current.next
            return
        

        # Declare variabes to hold the previos and current nodes..
        previous = None
        current = self.head

        


        # Traverse the linked list as we seacrh for the value
        while current:
            if current.data == value:
                previous.next = current.next
                current.next = None
                del current
                return
            previous = current
            current = current.next
            # Print value not found
        print("The value ",value,"Was not found in the linked list...")




    # The print list funtion....
    # It traverses the linked list while printing
    def printlist(self):
        currentNode = self.head
        while currentNode:
            print(currentNode.data,end="->")
            currentNode = currentNode.next
        print("None")
        


# Creating the linked list
mysinglylinkedlist = Singlylinkedlist()



# Calling the insert at the beginning funtion...
mysinglylinkedlist.insertatbeginning('D')
mysinglylinkedlist.insertatbeginning('C')
mysinglylinkedlist.insertatbeginning('B')
mysinglylinkedlist.insertatbeginning('A')
mysinglylinkedlist.insertatend("E")

# printing address of the linked list 
print(mysinglylinkedlist)

# printing contents of the list...
mysinglylinkedlist.printlist()
# testing the delete....
mysinglylinkedlist.deleteinbetween("C")
mysinglylinkedlist.printlist()



# Create a node by making an object of the node class
# Each node is allocated a contigous memory location....
# nodeA = Node("A")
# nodeB=Node("B")
# nodec = Node("C")


# accessing the data
# print(nodeA.data)

# linking the nodes together
# nodeA.next = nodeB

# Compare memories after linking
# print(nodeA.next)
# print(nodeB)

# nodeB.next = nodec


# Testing after the linking for data in the second node....
# print(nodeA.next.data)
# print(nodeB.next.data)

