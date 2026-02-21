#  Write a program that will swap numbers.

a = int(input("Enter first number : "))
b = int(input("Enter 2nd number : "))

print("a before swapping : ", a)
print("b before swapping : ", b)
temp = a
a = b
b = temp
print("--------------------")
print("a after swapping : ", a)
print("b after swapping : ", b )
