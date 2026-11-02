text = input("Enter text: ")
normalized = "".join(character.lower() for character in text if character.isalnum())
print("Palindrome" if normalized == normalized[::-1] else "Not palindrome")
