# Write a program that will give you the in hand salary after 
# deduction of HRA(10%),DA(5%),PF(3%), and tax(if salary is between 
# 5-10 lakh–10%),(11-20lakh–20%),(20< _   – 30%)(0-1lakh print k). 


salary = float(input("Enter your salary package : "))

if salary < 100000:
    print("k")
else:
    RHA = 0.1 * salary
    DA = 0.05 * salary
    PF = 0.03 * salary

    if salary > 500000 and salary < 1000000:
        tax = 0.1 * salary
    elif salary > 1000000 and salary < 2000000:
        tax = 0.2 * salary
    else:
        tax = 0.3 * salary
    total_deduction = RHA + DA + PF + tax
    in_hand = salary = total_deduction
    print("In hand salary = ", in_hand)
    









