min_hours = int(input())
max_hours = int(input())
sleep = int(input())

if sleep < min_hours:
    print("Deficiency")
else:
    if sleep > max_hours:
        print("Excess")
    else:
        print("Normal")
