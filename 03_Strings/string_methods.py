text = "  hello python world  "
print(text.strip())
print(text.upper(), text.lower(), text.title())
print(text.replace("python", "programming"))
print(text.count("o"), text.find("python"))
print("a,b,c".split(","))
print("-".join(["a", "b", "c"]))
print("123".isdigit(), "abc".isalpha(), "abc123".isalnum())
