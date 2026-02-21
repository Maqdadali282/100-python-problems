# Write a program that will tell the number of dogs and chicken are there when the user will provide the value of total heads and legs. 

heads = int(input("Enter total heads : "))
legs = int(input("Enter total legs : "))

if legs %2 != 0:
    print("invalid input !")
else:
    dogs = (legs - 2 * heads) / 2
    chicken = heads - dogs

    if dogs < 0 or chicken < 0 :
        print("No possible solution !")
    else:
        print("Dogs : ", int(dogs))
        print("Chicken : ", int(chicken))