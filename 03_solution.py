# User will input (2numbers).Write a program to swap the numbers 

a = int(input("Enter a : "))
b = int(input("Enter b : "))

temp = a
a = b
b = temp
print("a = ",a)
print("b = ",b)