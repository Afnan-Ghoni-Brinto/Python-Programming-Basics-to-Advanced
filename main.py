"""Interactive command-line calculator."""
def calculate(a, operator, b):
    if operator == "+": return a + b
    if operator == "-": return a - b
    if operator == "*": return a * b
    if operator == "/":
        if b == 0: raise ZeroDivisionError("Cannot divide by zero")
        return a / b
    raise ValueError("Choose +, -, *, or /")

def main():
    print("Calculator | enter q to quit")
    while True:
        first = input("First number (q to quit): ").strip()
        if first.lower() == "q": break
        try:
            a = float(first)
            operator = input("Operator (+ - * /): ").strip()
            b = float(input("Second number: "))
            print("Result:", calculate(a, operator, b))
        except (ValueError, ZeroDivisionError) as error:
            print("Error:", error)

if __name__ == "__main__":
    main()
