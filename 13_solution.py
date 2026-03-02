# . Write  a program that will tell whether the given number is divisible by 3 & 6. 

num = int(input("Enter the number : "))


if num % 3==0 and num % 6 == 0:
    print(f"The given number {num} is completely divisible by 3 and 6 ")
else:
    print("indivisible by 3 and 6")