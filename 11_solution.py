# Write a program to find the simple interest when the value of principle,rate of interest and time period is given. 


Principle = int(input("Enter the value of principle : "))
interst = int(input("Enter the value of rate of interest : "))
time_period = int(input("Enter the value of time_period : "))

simple_interest = Principle *interst * time_period /100

print("Total value of simple interest is = ", simple_interest)