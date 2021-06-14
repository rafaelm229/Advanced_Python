# Write a Python script to sort (ascending and descending)
#  a dictionary by value


import operator

mydict = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}

print("Original Dictionary:", mydict)

sorted_mydict = sorted(mydict.items(), key=operator.itemgetter(1))
print("Dictionary in ascending  order  by values:", sorted_mydict)

sorted_mydict = dict(sorted(mydict.items(), key=operator.itemgetter(1), reverse=True))

print("Dictionary in descending order by value :", sorted_mydict)

"""
Output:
    Original Dictionary: {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
    Dictionary in ascending  order  by values: [(0, 0), (2, 1), (1, 2), (4, 3), (3, 4)]
    Dictionary in descending order by value : {3: 4, 4: 3, 1: 2, 2: 1, 0: 0}

"""