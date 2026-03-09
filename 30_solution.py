# . User will provide 2 numbers you have to find the by LCM of those 2 numbers


num1 = float(input("Enter first number : "))
num2 = float(input("Enter second number : "))

original1 = num1
original2 = num2

while num2 !=0:
    reminder = num1 % num2
    num1 = num2
    num2 = reminder
hcf = num1
lcm = original1 * original2/ hcf
print("LCM is : ", lcm)