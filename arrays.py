from array import *


ages = array("i",[2,3,4,6,7])

print(ages)

# end of the array add an item
ages.append(55)
print(ages)


#start of the array
ages.insert(0,88)
print(ages)

# center of the array
ages.insert(3,76)
print(ages)


# Traversing an array
for x in ages :
    print(x)


def traversesrray(array):
    for elements in array:
        print(elements)


traversesrray(ages)