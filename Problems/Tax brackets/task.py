money = int(input())
tax = 0
percent = 0

if money < 15528:
    percent = 0
elif money < 42708:
    percent = 15
elif money < 132407:
    percent = 25
else:
    percent = 28

tax = money * (percent / 100)

print("The tax for {} is {}%. That is {:.0f} dollars!".format(money, percent, tax))
