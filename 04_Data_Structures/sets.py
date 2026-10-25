a = {1, 2, 3, 3}
b = {3, 4, 5}
print("Unique:", a)
print("Union:", a | b)
print("Intersection:", a & b)
print("Difference:", a - b)
print("Symmetric difference:", a ^ b)
a.add(10)
a.discard(2)
print("Updated:", a)
