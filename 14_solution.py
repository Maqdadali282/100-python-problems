temp = float(input("Enter the value of temperature : "))
humidity = float(input("Enter the value of humidity : "))

if (temp  >= 30 and humidity >=90):
    print("Hot and Humid!")

elif temp >=30 and humidity <90:
    print("Hot")
elif temp < 30 and humidity >=90:
    print("cool and humid")
else:
    print("cool") 