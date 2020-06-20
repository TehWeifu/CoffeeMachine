name = input().split()
best_name = name

while name[0] != "MEOW":
    if int(name[1]) > int(best_name[1]):
        best_name = name
    name = input().split()

print(best_name[0])
