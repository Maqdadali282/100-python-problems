# . Write a program that will tell whether the given year is a leap year 
# or not. 


year = int(input("Enter the year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("The given", year, "is a leap year")
else:
    print("The given", year, "is not a leap year")
