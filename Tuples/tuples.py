# tuples: ordered, immutable, allows duplicate elements

mytuple = ("Max", 5, "Boston")
print(mytuple)

mytuple_with_one_item = ("max")  # without a comma "," the compiler will not recognizer as a tuple, but a str

mytuple_with_one_item = ("Max",)

#tuple fucntion 

mytuple = tuple(["Max", 5, "Boston"]) # -> tuple


for i in mytuple:
    print(i)


if "Max" in mytuple:
    print("yes")
else:
    print("no")

mytuple = ("R","a","f","e","l")

print(len(mytuple)) # 5


print(mytuple.count("e"))
