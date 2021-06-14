# Dictionary: key-value pairs, unordered, mutable
# Dicts going well with tuples but will not gong to work with Lists.

mydict = {"name": "max", "age": 28, "city": "New York"}
print(mydict)

mydict2 = dict(name="Rafael", age=25, city="Boston" )
print(mydict2)

value = mydict["age"]
print(value)

mydict = ["email"] = "max@xyz.com"
print(mydict)

del mydict["name"]
print(mydict)

mydict.pop("age")
print(mydict)

mydict.popitem()
print(mydict)

try:
    print(mydict["name"])
except:
    print("error")


for key in mydict: # print all keys
    print(key)

for key, value in mydict:
    print(key, value)

mytuple = (7,8)

mydict3 = {mytuple: 15}

print(mydict3)

