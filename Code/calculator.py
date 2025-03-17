# Basic Python Calculator made with ❤️ by Blessed
# Get user inputs
num1 = int(input("Enter the first number: ")) # First number
num2 = int(input("Enter the second number: ")) # Second number
operation = input("Enter the operation (+, -, *, /): ") # Operation

# Perform calculation based on operation
if operation == '+':
    result = num1 + num2
    print(f"{num1} + {num2} = {result}")
elif operation == '-':
    result = num1 - num2
    print(f"{num1} - {num2} = {result}")
elif operation == '*':
    result = num1 * num2
    print(f"{num1} * {num2} = {result}")
elif operation == '/':
    if num2 != 0:  # Check for division by zero
        result = num1 / num2
        print(f"{num1} / {num2} = {result}")
    else:
        print("Error: Cannot divide by zero")
else:
    print("Invalid operation. Please use +, -, *, or /")