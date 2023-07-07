import sys

try:
    x = int(input("X: "))
    y = int(input("X: "))
except ValueError:
    print("Error: String cannot convert to to int")
    sys.exit(1)

try:
    result = x / y
    print(f"{x}/{y} is equal to {result}")
except ZeroDivisionError:
    print("Error: Cannot divide by 0")
    sys.exit(1)

# print(f"{x}/{y} is equal to {result}")