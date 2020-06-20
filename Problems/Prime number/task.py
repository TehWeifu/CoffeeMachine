number = int(input())
if number < 2:
    print("This number is not prime")
elif number == 2:
    print("This number is prime")
else:
    for num in range(2, number):
        if number % num == 0:
            print("This number is not prime")
            break
    else:
        print("This number is prime")
