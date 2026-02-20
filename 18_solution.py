# 1. Write a menu driven program - 1.cm to ft  2.kl to miles  3.usd to inr  4.exit 

while True:
    print("1. cm to feet : ")
    print("2. km to miles : ")
    print("3. usdt to pkr : ")
    print("4. exit")
    choice = int(input("Enter your choice : "))

    if choice == 1:
        cm = float(input("Enter centimeter : "))
        feet = cm / 30.48
        print(f"{cm} equal in feet {feet} ")
        break
    elif choice == 2:
        km = float(input("Enter distance into km : "))
        miles = km * 0.6213
        print(f"{km} is equal to {miles}")
        break
    elif choice == 3:
        usdt = float(input("Enter total usdt : "))
        pkr = usdt * 280
        print(f"{usdt } is equal to {pkr}")
        break
    elif choice == 4:
        print("program is exact")
        break