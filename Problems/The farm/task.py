money = int(input())

if money < 23:
    print("None")
elif money < 678:
    if money < 46:
        print("1 chicken")
    else:
        print(money // 23, "chickens")
elif money < 1296:
    print("1 goat")
elif money < 3848:
    if money < 2592:
        print("1 pig")
    else:
        print("2 pigs")
elif money < 6769:
    print("1 cow")
elif money < 13538:
    print("1 sheep")
else:
    print(money // 6769, "sheep")
