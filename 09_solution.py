# Write a program that take a user inputr of three angles and will find out whether it can form a triangle or not. 


try:
    a1 = int(input("Enter the first angle : "))
    a2 = int(input("Enter the  2nd angle : "))
    a3 = int(input("Enter the 3rd angle : "))
    
    if a1>0 and a2 > 0 and a3>0:
        if a1 + a2 + a3 == 180:
            print("this is a valid triangle")
        else:
            print("this is not a valid triangle!")
    else:
        print("Angle must be greater then 0")
except ValueError:
    print("Enter valid value")