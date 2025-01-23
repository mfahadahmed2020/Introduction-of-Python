# Ye Sir ny Revision or baki krwaya tha:
# Isme sy kuch galat lage to bata dena.

# 1. Python Install
# 2. CMD | python --version | python | print("Hello, World!")
# 3. VSCODE | Create Python Folder | VSCODE-File-Open Folder-Then Select New File
# 4. print("Hello, World!")
# 5. Folder | Upper Link | Clear Path | CMD
# 6. Variable = To Store Data
name: str = "Andrew"
age: int = 20
in_active: bool = True
print(name)
print(age)
print(in_active)

# 7. Comment (#)

# 8. Operators: 
# || Arithmetic operators || 
x = 10
y = 3
print(x + y)     #Addition       : 13
print(x - y)     #Subtraction    : 7
print(x * y)     #Multiplication : 30
print(x / y)     #Division       : 3.3333....
print(x // y)    #Floor Division : 3 (Decimal ko hata deta hai/ divide me upr wala)
print(x % y)     #Modulus        : 1 (remainder)
print(x ** y)    #Exponentiation : 1000 (10^3 or 10*10*10)
num1: int = 5
num2: int = 5
sum: int = num1 + num2
print(sum)

# || Asignment operators || 
# Value ko assign krne k liye jo operator use hota (=)
x: int = 15
x = x + 5
print(x)

# || Comparison operators || True/False 
# == (equal to)
# >  (greater than equal to)
# < (less than)
# >= (greater than equal to)
# <= (less than equal to)
# != (not equal to)

num1: int = 10
num2: int = 11
print(num1 == num2)  #False
print(num1 > num2)   #False
print(num1 < num2)   #True
print(num1 >= num2)  #False
print(num1 <= num2)  #True
print(num1 != num2)  #True


# || Logical operators ||
# and, or, not

# condition (and)
num1: int = 40
num2: int = 11
print(num1 > 10 and num1 < 30) #False
# num1 is greater than 10 AND num1 is less than 30
# (and) condition me puri condition thek honi chahiye


# condition (or)
num1: int = 40
num2: int = 11
print(num1 > 10 or num1 < 30) #True
# (or) condition me koi ek thek honi chahiye

#Ghar py 2 cheezen hain ek ups and ek k_electric

k_electric: "no k_electric"
ups: "no ups"
print("k_electric" == "no k_electric" or "ups" != "no ups") 

# condition (not)
# condition true hogi to false hojaegi or agr false hogi to true hojaegi 

# || IF ELSE ||
# if - agr
# else - wrna

# indentations - Double space sy if k bad wali line me jo bhi likhogy to if ki condition me aega

num1: int = 2
num2: int = 1
if num1>1:
    print("Hello")
    uname="Sir Sohaib"
    print(uname)
