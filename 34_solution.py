# Write a Python program that accepts an integer (n) and computes the value of n+nn+nnn. 

num = int(input("Enter the integer : "))

nn = num * 10 + num
nnn = num * 100 + num * 10 + num
result = num + nn + nnn
print("Result : ", result)