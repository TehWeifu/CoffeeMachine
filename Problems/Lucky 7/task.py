number_values = int(input())

for counter in range(0, number_values):
    number = int(input())
    if number % 7 == 0:
        print(number * number)
