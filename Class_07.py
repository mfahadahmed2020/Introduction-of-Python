print("Mini Calculator")
num1=float(input("Entre a First Number Here:"))
num2=float(input("Entre a Second Number Here:"))
choice=int(input("Entre Number Between 1-4"))
print(""""
Preee 1 For Addition
Preee 2 For Substraction
Preee 3 For Multiplication
Preee 4 For Division
      """)
if choice==1:
    sum= num1+num2
    print("The Addition of Two Give Number is",sum)
elif choice==2:
        print("The Substraction of Two Give Number is",num1-num2)
elif choice==3:
        print("The Multiplication of Two Give Number is",num1*num2)
elif choice==4:
        print("The Division of Two Give Number is",num1/num2)
else:
    ("Invalid Input Bhai Sahi Number Select Kar")