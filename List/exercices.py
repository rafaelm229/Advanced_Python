''' 
Exercices
Link: https://towardsdatascience.com/60-questions-to-test-your-knowledge-of-python-lists-cca0ebfa0582
'''


# 1. Check if a list contains an element
li = [1,2,3,'a','b','c']

'a' in li 



# 2. How to iterate over 2+ lists at the same time

name = ['Snowball', 'Chewy', 'Bubbles', 'Gruff']
animal = ['Cat', 'Dog', 'Fish', 'Goat']
age = [1, 2, 2, 6]

# You can zip() lists and then iterate over the zip object. 
# A zip object is an iterator of tuples.

z = zip(name,animal,age)

for name,animal,age in z:
    print("%s the %s is %s" % (name,animal,age))



# 3. When would you use a list vs dictionary?

'''
Lists and dictionary generally have slightly different use cases but there is some overlap.
The general rule of algorithm questions I’ve come to is that if you can use both, use a dictionary because lookups are faster.
List
Use a list if you need to store the order of something.
Ie: id’s of database records in the order they’ll be displayed.
'''
ids = [23,1,7,9]
'''
While both lists and dictionaries are ordered as of python 3.7, a list allows duplicate values while a dictionary doesn’t allow duplicate keys.
Dictionary
Use a dictionary if you want to count occurrences of something. Like the number of pets in a home.
'''
pets = {'dogs':2,'cats':1,'fish':5}
'''
Each key can only exist once in a dictionary. Note that keys can also be other immutable data structures like tuples. Ie: {('a',1):1, ('b',2):1}.

'''


# 4. Is a list mutable?
# Yes. Notice in the code below how the value associated with the same
#  identifier in memory has not changed.

x = [1]
print(id(x),':',x) #=> 4501046920 : [1]
x.append(5)
x.extend([6,7])
print(id(x),':',x) #=> 4501046920 : [1, 5, 6, 7]

# 5. Does a list need to be homogeneous?
# No. Different types of object can be mixed together in a list.

a = [1,'a',1.0,[]]
a #=> [1, 'a', 1.0, []]


# 6. What is the difference between append and extend?

# .append() adds an object to the end of a list.
a = [1,2,3]
a.append(4)
a #=> [1, 2, 3, 4]

# This also means appending a list adds that whole list as a 
# single element, rather than appending each of its values.

a.append([5,6])
a #=> [1, 2, 3, 4, [5, 6]]


# .extend() adds each value from a 2nd list as its own element. 
# So extending a list with another list combines their values.

b = [1,2,3]
b.extend([5,6])
b #=> [1, 2, 3, 5, 6]


  