#sum of numbers and also check whether the sum of the number is even or odd
num1=int(input("enter the number1:"))
num2=int(input("enter the number2:"))
sum=num1+num2
if sum%2==0:
    print(f"the given number is even number:{sum}")
else:
    print(f"the given number is odd number:{sum}")