# Write a program that will reverse a four digit number.Also it checks 
# whether the reverse is true. 

num = int(input("Enter four digit number : "))

original = num
reverse = 0
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num//10

print("Reverse number ", reverse)

if original == reverse:
    print("The reverse is true ")
else:
    print("The reverse is not TRUE")