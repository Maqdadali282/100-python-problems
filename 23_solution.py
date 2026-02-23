# Write a program that can find the factorial of a given number provided by the user. 

# num = int(input("Enter the number you want to find facorial : "))
# result = 1
# for i in range(1,num + 1):
#     result = result * i
# print("facorial : ", result)

#using function to find factorial


def factorial(num):
    if num ==0 or num ==1:
        return 1
    else:
        return num * factorial(num-1)

print(factorial(5))