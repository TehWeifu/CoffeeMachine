number_of_values = int(input())
mean = 0.0

for counter in range(0, number_of_values):
    number = int(input())
    mean += number

print(mean / number_of_values)
