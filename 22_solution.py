#  Write a program that can multiply 2 numbers provided by the user without using the * operator. 

# Take input
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = 0

# Handle negative numbers
negative = False
if num2 < 0:
    negative = True
    num2 = -num2

# Repeated addition
for i in range(num2):
    result += num1

# Apply negative sign if needed
if negative:
    result = -result

print("Multiplication result:", result)