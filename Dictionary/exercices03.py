#  Write a Python script to concatenate following dictionaries to create 
# a new one.

"""
Sample Dictionary :
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

"""

dictone = {1:10, 2:20}
dicttwo = {3:30, 4:40}
dictthree = {5:50, 6:60}
dictfour = {}

for d in (dictone, dicttwo, dictthree): dictfour.update(d)
print(dictfour)


"""
Output:
{1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
"""