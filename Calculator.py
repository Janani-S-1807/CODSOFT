def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Division by zero is not allowed."
    return a / b

print("Simple Calculator")

number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

print("\nSelect an Operation")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter your choice (1-4): ")

if choice == "1":
    print("Result:", add(number1, number2))
elif choice == "2":
    print("Result:", subtract(number1, number2))
elif choice == "3":
    print("Result:", multiply(number1, number2))
elif choice == "4":
    print("Result:", divide(number1, number2))
else:
    print("Invalid choice. Please run the program again.")