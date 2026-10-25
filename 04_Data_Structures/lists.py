fruits = ["apple", "banana", "mango"]
fruits.append("orange")
fruits.insert(1, "guava")
fruits.remove("banana")
print("List:", fruits)
print("First:", fruits[0], "Last:", fruits[-1])
for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)
print("Sorted copy:", sorted(fruits))
print("Original:", fruits)
