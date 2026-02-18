# Write a program that will take three digits from the user and add the square of each digit. 

num1  = int(input("Enter the first number : "))
num2  = int(input("Enter the 2nd number : "))
num3  = int(input("Enter the 3rd number : "))

result  = num1**2 + num2**2 + num3**2
print(f"Square of the given numbers are : {num1**2} , {num2**2} , {num3**2}")
print(f"The square sum of the given number is : {result}") 