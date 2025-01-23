# 1. Arithematic operators  
# 2. Assigment operators
# 3. Comparison operators (boolean) TrueFalse
# 4. Logical operators


#  1. Arithematic operators  

#  7 + 5 = 12
print(7 + 5)
print(10 - 5)
print(10 * 2)
#     5 X 2
print(5 / 2)  
# exponent  8^2 = 8 X 8
print(8 , 2)  
# floor division
print(11 , 2) 
#      11  2 = 1  remainder  modulus
print(11 % 2)

num1: int = 5  # type: ignore
num2: int = 5 # type: ignore

#           5   +  5
sum: int = num1 + num2 # type: ignore
#           5   -  5
sub: int = num1 - num2 # type: ignore
#           5     5
div: int = num1 * num2 # type: ignore
#           5   x  5
nmu1: int = num1 / num2 # type: ignore
print(nmu1) # type: ignore

# 2. Assigment operators

x : int = 15 # type: ignore
#  15 + 5 = 15
x = x + 5 # type: ignore
# x = x - 5
# x = x  2

# x int = 15
#   15  2 = 30
# remainder  modulus
# x = x % 3 

print(x)

# 3. Comparison operators (TrueFalse)
#  ==   (equal to) 
#      (greater than)
#      (less than)
#  =   (greater or equal to)
#  =    (less than or equal to)
#  !=    (not equal to)

#  mera pehla operandvalue  
# dusre wale operandvalue k baraber he

num1: int = 10  # type: ignore
num2: int = 11 # type: ignore
# print(10 == 10)
print(num1 == num2) # type: ignore
print(num2 / num1) # type: ignore
print(num2 - num1) # type: ignore
print(num1 + num2 ) # type: ignore
print(num1 * num2) # type: ignore
print(num1 != num2) # type: ignore

# Logical operators
#  and, or , not
#  or, True & False

num1: int = 20
num2: int = 25
print(num1 < 10 and num1 > 30)
print(num1 !=20 and num2 > 50)