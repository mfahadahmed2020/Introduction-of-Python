Class_06 = "Coding Work With Python By Sir Aneeq"
print(Class_06)

# Range Function/Method

numbers =  [1,2,3,4,5,6,7,8,9]
x = range(1,10)  # 1,2,3,4,5
# 1.starting point
# 2.condition
# 3.increment
print(numbers)
print(list(x))

#  Aam Zindagi
num: int = 2 
print("2 x 1 =", num * 1  )
print("2 x 2 =", num * 2  )
print("2 x 3 =", num * 3  )
print("2 x 4 =", num * 4  )
print("2 x 5 =", num * 5  )
print("2 x 6 =", num * 6  )
print("2 x 7 =", num * 7  )
print("2 x 8 =", num * 8  )
print("2 x 9 =", num * 9  )
print("2 x 10 =", num * 10 )


# Mintos Zindagi
for num in range(1,11): # 1,2,3,4,... ,10
     print("2 x",num , "=", 2 * num)          # indentation
     print(f"2 x {num} = {2 * num}") # fstring

#loops
# 1. for loop
# 2. while loop 


num = 1
num = num + 1
print("Num First Time", num)
num = num + 1
print("Num Second Time", num)
print(num < 10)
while num >= 10:
     print("Number Before Increment", num)
num = num + 1
print("Number After Increment", num)

password: str = "Python123"
user_input: str = ""

print("user_input != password is",user_input != password)
while user_input == password: # User Input Wo Baraber Na Ho Password K 
     print("Correct Password")
user_input = input("Type Your Answer Please")
print("Correct Password is Welcome")


# String
# Integer
# Boolean
# List
# Tuple

numbers = [1,2,3,4,5]
#         0   ,   1   ,  2    ,  3
names1 = ["Ali","Bilal","Hamza","Okasha"]  # List  Mutable
#         0   ,   1   ,  2    ,  3
names2 = ("Ali", "Bilal", "Hamza", "Okasha") # Tuple Immutable
name: str  = "Ali"
name  = "Bilal"
print("name is", name)

#  List
print("Names1 Before Over Write", names1)
Bilal    =  "Abdullah"
names1[2] = "Abdullah"
print("Names1 After Over Write", names1)


#  Tuple
print("Names2 Before Over Write", names2)
Bilal    =  "Abdullah"
names1 = "Abdullah"
print("Names2 After Over Write", names2)


print("List First Name is", names1[0])
print("Tuple First Name is", names2[0])