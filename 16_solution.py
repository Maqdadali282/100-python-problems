#  Write a program that will check whether the number is armstrong number or not. 


num = int(input("Enter the number you want to check , armstrong or not : "))

string = str(num)
length = len(str(num))
total = 0

for digit in str(num):
    total +=int(digit)** length
if total == num:
    print("Armstrong number ")
else:
    print("Not an Armstrong number")
    
