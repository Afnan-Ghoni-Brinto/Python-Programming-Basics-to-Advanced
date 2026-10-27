try:
    numerator = float(input("Numerator: "))
    denominator = float(input("Denominator: "))
    result = numerator / denominator
except ValueError:
    print("Please enter numbers.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
else:
    print("Result:", result)
finally:
    print("Calculation finished.")
