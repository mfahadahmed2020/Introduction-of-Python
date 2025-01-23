Class_05 = "Coding Work With Python By Sir Aneeq"
print(Class_05)
# condition -> True/False
if False:
    print("condition is true")
else:
    print("condition is false")

# comparison operators -> True / False
num: int = 10
print(num < 10)  # False
print(num > 0)  # True

if num > 0:  # اگر num صفر سے بڑا ہو
    print("number is positive")
else:
    print("number is negative")

num: int = 100  # True اور False
print(num > 0 and num < 100)  # False
if num > 0 and num < 100:
    print("number is positive")
else:
    print("number is negative")

# String comparison
name: str = "Sir Ali"

if name == "Sir Sohaib":
    print("welcome Sir Sohaib")
else:
    print("App Kon")

print("Kesse hen Aap")

# Snake case variable
time_of_day: str = "abc"

if time_of_day == "morning":
    print("Good Morning")
elif time_of_day == "afternoon":
    print("Good AfterNoon")
elif time_of_day == "evening":
    print("Good Evening")
else:
    print("Good Night")

# List example
names: list[str] = ["Sir Aneeq", "Sir Sohaib", "Sir Sami"]
print(names)  # مکمل لسٹ پرنٹ کرے گا
print(names[1])  # "Sir Sohaib" پرنٹ کرے گا

# Range example
numbers: list[int] = [1, 2, 3, 4, 5]
print(numbers[4])  # 5 پرنٹ کرے گا

if numbers[0] > 1:
    print("First number is greater than 1")

res = range(1, 5)
print(list(res))

number2 = list(range(1, 5))
print(number2)

# For loop example
for n in numbers:
    print("n is", n)

# Final example
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Aam Zindagi")
print(numbers[0])
print(numbers[1])
print(numbers[2])
print(numbers[3])
print(numbers[4])

print("Mintos Zindagi")
for num in numbers:
    print(num)