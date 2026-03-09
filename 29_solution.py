# . User will provide 2 numbers you have to find the HCF of those 2 numbers 


num1 = float(input("Enter first number : "))
num2 = float(input("Enter second number : "))

while num2 !=0:
    reminder = num1 % num2
    num1 = num2
    num2 = reminder
print(num1)