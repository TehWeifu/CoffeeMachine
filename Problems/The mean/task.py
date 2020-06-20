total_sum = 0
counter = 0
menu = input()

while menu != ".":
    total_sum += int(menu)
    counter += 1
    menu = input()

print(total_sum / counter)
