# 1. Assignment one :
# 1. Addition, Subtraction, Multiplication & Division Functions (Dynamic Function)

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Division By Zero is Not Allowed"
        print("Division By Zero is Not Allowed")

# 2. Assignment Two :
# 2. Create A Calculator Using Functions
#    Dynamic Function

def calculator():
    print("Choose an operation: +, -, *, /")
    operation = input("Enter operation: ")
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    if operation == "+":
        print("Result:", add(num1, num2))
    elif operation == "-":
        print("Result:", subtract(num1, num2))
    elif operation == "*":
        print("Result:", multiply(num1, num2))
    elif operation == "/":
        print("Result:", divide(num1, num2))
    else:
        print("Invalid operation")

calculator()

# 3. Assignment Three :
# 3.Research on Default Parameters & Use-Case

def greet(name="Guest"):
    return f"Hello, {name}!"

# Use-Case:
print(greet())           # Default Parameter Will Be Used
print(greet("Ali"))      # Provided Parameter Will Overwrite Default

# Second Use-Case

def greet(name="Guest", times=11):
    for i in range(times):
        print(f"Perfect, {times}!")

# Using Default Parameters
greet()                # Default Name & Times
greet("Ali")           # Custom Name & Default Times
greet("Ali", 11)       # Custom Name & Custom Times