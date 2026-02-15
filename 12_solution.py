#  Write a program to find the volume of the cylinder. Also find the  cost when ,when the cost of 1litre milk is 40Rs. 

height = float(input("Enter the height of the cylinder : "))
radius = float(input("Enter the radius of the cylinder : "))
pi = 3.14

volume = pi * radius**2 * height
litres = volume / 1000
cost = litres * 40

print("total volume is : ", volume)
print("total litres  is : ", litres)
print("total cost per litre is : ", cost)
