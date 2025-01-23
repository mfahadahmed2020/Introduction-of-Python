# Class_06 Example
Class_06 = "Coding Work With Python By Sir Aneeq"
print(Class_06)

# Range Function/Method
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
x = range(1, 10)  # 1,2,3,...9
print(numbers)
print(list(x))

# Multiplication Table - Aam Zindagi
num: int = 2
print("2 x 1 =", num * 1)
print("2 x 2 =", num * 2)
print("2 x 3 =", num * 3)
print("2 x 4 =", num * 4)
print("2 x 5 =", num * 5)
print("2 x 6 =", num * 6)
print("2 x 7 =", num * 7)
print("2 x 8 =", num * 8)
print("2 x 9 =", num * 9)
print("2 x 10 =", num * 10)

# Multiplication Table - Mintos Zindagi
for num in range(1, 11):  # 1,2,3,...,10
    print(f"2 x {num} = {2 * num}")

# Loops
# 1. For Loop
# 2. While Loop

# Example of While Loop
num = 1
while num < 10:
    print("number before increment:", num)
    num += 1
print("number after increment:", num)

# Password Check with While Loop
password: str = "python123"
user_input: str = ""

while user_input != password:  # Jab Tak User Input Password Ke Barabar Na Ho
    print("Incorrect password!")
    user_input = input("Type your password: ") # User Se Input Lena

print("Correct password! Welcome!")

# Lists and Tuples
numbers = [1, 2, 3, 4, 5]
names1 = ["Ali", "Bilal", "Hamza", "Okasha"]  # List (Mutable)
names2 = ("Ali", "Bilal", "Hamza", "Okasha")  # Tuple (Immutable)

# List Example
print("names1 before overwrite:", names1)
names1[1] = "Abdullah"
print("names1 after overwrite:", names1)

# Tuple Example
print("names2 is immutable:", names2)

# Accessing List and Tuple Elements
print("List first name is:", names1[0])
print("Tuple first name is:", names2[0])