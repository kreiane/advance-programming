import operator

def add(x, y):
    return operator.add(x, y)

def subtract(x, y):
    return operator.sub(x, y)

def multiply(x, y):
    return operator.mul(x, y)

def divide(x, y):
    if y != 0:
        return operator.truediv(x, y)
    else:
        return "Cannot divide by zero."

def modulus(x, y):
    return operator.mod(x, y)

def check_greater(x, y):
    return operator.gt(x, y)

print("Calculator Menu:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Modulus")
print("6. Check greater number")

choice = int(input("Enter your choice (1-6): "))

x = float(input("Enter the first number: "))
y = float(input("Enter the second number: "))

if choice == 1:
    result = add(x, y)
elif choice == 2:
    result = subtract(x, y)
elif choice == 3:
    result = multiply(x, y)
elif choice == 4:
    result = divide(x, y)
elif choice == 5:
    result = modulus(x, y)
elif choice == 6:
    result = check_greater(x, y)
else:
    result = "Invalid choice. Please choose a number from 1 to 6."

print("Result:", result)