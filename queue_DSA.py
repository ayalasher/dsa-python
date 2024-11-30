print("Queue below : ")
class queue:
    def __init__(self,maxsize):
        self.list=[]
        self.maxsize = maxsize
    

    def isempty(self):
        return self.list == [] 
    
    def printqueue(self):
        if self.isempty():
            print("The queue is empty")

        for item in self.list:
           print(item) 
    def enqueue(self,item):
        if len(self.list) == (self.maxsize):
            print("The queue is full")
            return
        
        self.list.append(item)

    def dequeue(self):
        if self.isempty():
            print("The queue is empty")
            return
        self.list.pop(0)

    def peek(self):
        if self.isempty():
            print("The queue is empty")
            return
        return self.list[0]



# Create queue of fruits
fruits = queue(3)

fruits.enqueue("Apple")
fruits.enqueue("Banana")
fruits.enqueue("Mango")
fruits.enqueue("Pineapple")


fruits.printqueue()
print(f"Item at the peek is :  {fruits.peek()} ")

        
