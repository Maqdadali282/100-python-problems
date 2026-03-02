# Write a program to print all the unique combinations of 1,2,3 and 4.


count = 0

for i in [1, 2, 3, 4]:
    for j in [1, 2, 3, 4]:
        for k in [1, 2, 3, 4]:
            for l in [1, 2, 3, 4]:
                if len({i, j, k, l}) == 4:   # ensures no repetition
                    print(i, j, k, l)
                    count += 1

print("Total combinations:", count)