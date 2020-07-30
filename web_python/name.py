"""
#formatting
#====
name = input("name: ")
print("Hello, "+ name)
print("Hello, {name}")
print(f"Hello, {name}")

"""

"""
#Condition
#====
#input function always return 'str' type
n = int(input("number: ")) 
if n > 0:
    print("n is positive")
elif n < 0:
    print("n is negative")
else: 
    print("n is zero")
"""


"""
#Sequence
#====
name = "Harry"
print(name[0])
#....List (sequence of mutable values)
names = ["Harry", "Kris", "Tom"]
print(names)
print(names[0])

names.append("Teddy")
names.sort()

#....Tuple (sequence of immutable values)
coordinateX = 10.0
coordinateY = 20.0
coordinate = (10.0, 20.0)
#....Set (collection of unique values)
s = set()
s.add(1)
s.add(3)
s.add(4)
s.add(2)
s.add(2)
s.remove(1)
print(s)
print(f"The set has {len(s)} elements")
#....Dict (collection of key-value pairs)
houses = {"Harry": "Gryffindor", "Draco": "Slytherin"}
print(houses["Harry"])
houses["Hermione"] = "Gryffindor"
print(houses["Hermione"])

"""


"""
#Loops
#===
for i in range(6):
    print(i)

names = ["Harry", "Kris", "Tom"]
for name in names:
    print(name)
name = "Kris"
for c in name:
    print(c)

"""

#function modules
#===
from functions import square
for i in range(10):
    print(f"The square of {i} is {square(i)}")
    
import functions
for i in range(10):
    print(f"The square of {i} is {functions.square(i)}")
