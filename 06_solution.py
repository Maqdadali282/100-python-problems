# Write a program that will tell whether the number entered by the 
# user is odd or even. 

num = int(input("Enter the number : "))
if num % 2 == 0:
    print("The given number is even")
else:
    print("The given number is odd")

# using function
def even_odd_number(num):
    if num % 2 == 0:
        print("even number")
    else:
        print("odd number")

even_odd_number(345)