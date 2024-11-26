print("Working with linked lists")
# A linked  list has the head , the node and the end.... train format


# creating the node class
class Node:
    # Initilisation funtion
    def __init__(self,data):
        self.data = data
        self.next = None


# Creating a linked list to implement a linked list operation 
class Singlylinkedlist:
    # Initialization funtion
    # Creating the head of the linked list
    def __init__(self,):
        self.head = None


    def insertatbeginning(self,data):
        # Creating the node
        newnode = Node(data)
        # Check if the hed is empty
        if self.head is None:
            self.head = newnode
        else:
            # Point the newnode to the head
            newnode.next = self.head
            self.head = newnode
        

mysinglylinkedlist = Singlylinkedlist()

mysinglylinkedlist.insertatbeginning('D')
mysinglylinkedlist.insertatbeginning('C')
mysinglylinkedlist.insertatbeginning('B')
mysinglylinkedlist.insertatbeginning('A')
print(mysinglylinkedlist)

# Create a node by making an object of the node class
# nodeA = Node("A")
# nodeB=Node("B")
# nodec = Node("C")


# accessing the data
# print(nodeA.data)

# linking the nodes together
# nodeA.next = nodeB

# # Compare memories after linking
# print(nodeA.next)
# print(nodeB)

# nodeB.next = nodec


# # Testing after the linking
# print(nodeA.next.data)

