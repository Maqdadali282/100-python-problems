# Take a number from the user and find the number of digits in it. 

#First method converting to string
# num = int(input("Enter the number : "))

# digits = len(str(num))
# print(digits)

#Second method  for integer
number = int(input("Enter the number : "))
number = abs(number)
count = 0

if number == 0:
    count = 1
else:
    while number > 0:
        number = number // 10
        count+=1

print(f"total digits in the given number are {count}")