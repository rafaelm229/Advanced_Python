# List: ordered, mutable, allows duplicade elements

from typing import List, Sequence


mylist = [ "banana", "cherry", "apple"]
print(List)


mylist2 = [5,True,"pineapple"]
print(mylist2)

item = mylist[2]
print(item)

for i in mylist:
    print(i)

if "banana" in mylist:
    print("yes")
else:
    print("no")


# to append a item in the list:
mylist.append("lemmon")
print(mylist)

# insert a item in a specific position:
mylist.insert(1,"blueberry")
print(mylist)

#to remove the last item in the list:
item = mylist.pop()
print(item)

#to remove a specific item use:
item = mylist.remove("cherry")
print(item)

#to remove all elements in the list:
item = mylist.clear()
print(item)

#to reverse the list:
item = mylist.reverse()
print(item)

# to sort you can use sort method.
item = mylist.sort()
print(item)

#slice

item = mylist[2:3]
print(item)

# to cpy a list 

mylist3 = mylist.copy()

# we can also use the list fucntion

mylist3 = list(mylist)

#advance Topic list comprehension:

Original_list = [1,2,3,4,5,6]

Squared_list = [i * i for i in Original_list]

print(Original_list)
print(Squared_list)

