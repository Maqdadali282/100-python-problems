#  Print all the armstrong numbers in the range of 100 to 1000.



for num in range(100,1000):
    original = num
    temp = num
    total = 0

    while temp > 0:
        digit = temp % 10
        total += digit ** 3
        temp = temp // 10

    if total == original:
        print(num)