#  Print the first 20 numbers of a Fibonacci series 


num0 = 0
num1 = 1
print(num0)
print(num1)

count = 0
while count < 20:
    next = num0 + num1
    num0 = num1
    num1 = next
    count+=1
    print(next)