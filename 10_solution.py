# Write a program that will take user input of cost price and selling price and determines whether its a loss or a profit


cost = int(input("Enter your cost price : "))
sell = int(input("Enter your selling price : "))


if sell > cost:
    profit = sell - cost
    print("profit : ", profit)
elif sell < cost:
    loss = cost - sell
    print("loss = ", loss)
else:
    print("no loss and profit")