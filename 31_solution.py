#  Print first 25 prime numbers

count = 0
num = 2

while count < 25:
    isPrime = True

    for i in range(2, num):
        if num % i == 0:
            isPrime = False
            break

    if isPrime:
        print(num)
        count = count + 1

    num = num + 1