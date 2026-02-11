#  Write a program to find the euclidean distance between two 
# coordinates. 

import math

x1 = int(input("Enter the value for x1 : "))
x2 = int(input("Enter the value for x2 : "))
y1 = int(input("Enter the value for y1 : "))
y2 = int(input("Enter the value for y2 : "))

euclidean_distance = math.sqrt((x2 - x1)**2 + ( y2 - y1))**2
print("total euclidean distance is :", euclidean_distance)