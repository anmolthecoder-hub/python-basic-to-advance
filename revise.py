# 3 inputs
num1=int(input("enter the first number:"))
num2=int(input("enter the second number:"))
num3=int(input("enter the third number:"))

if num1>num2 and num1>num3:
    print(num1, " is greater number")
    if num2>num3:
        print(num2, " is middle number")
        print(num3, "is smallest")
    elif num3>num2:
        print(num3," is middle")
        print(num2," is lowest")
        

elif num2>num1 and num2>num3:
    print(num2 , " is a greatest number")
    if num1>num3:
        print(num1," is middle number")
        print(num3, " is lowest number")
    elif num3>num1:
        print(num3," is middle number")
        print(num1, " is lowest number")


elif num3>num1 and num3>num2:
    print(num3, " is greater")
    if num1>num2:
        print(num1," is middle number")
        print(num2, "is lowest")
    elif num2>num1:
        print(num2," is middle number")
        print(num1, "is lowest")
