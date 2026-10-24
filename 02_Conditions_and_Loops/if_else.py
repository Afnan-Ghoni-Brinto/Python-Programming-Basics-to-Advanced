score = int(input("Enter score (0-100): "))
if not 0 <= score <= 100:
    print("Invalid score")
elif score >= 80:
    print("Grade A+")
elif score >= 70:
    print("Grade A")
elif score >= 60:
    print("Grade B")
elif score >= 50:
    print("Grade C")
else:
    print("Grade F")
