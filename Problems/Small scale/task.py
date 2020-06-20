num = input()
min_num = num

while str(num) != '.':
    if float(num) < float(min_num):
        min_num = num
    num = input()

print(min_num)
