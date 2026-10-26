import random
print("Dice roll:", random.randint(1, 6))
fruits = ["apple", "banana", "mango"]
print("Random fruit:", random.choice(fruits))
random.shuffle(fruits)
print("Shuffled:", fruits)
# For passwords and security tokens, use the secrets module instead.
