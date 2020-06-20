scores = input().split()
# put your python code here
c_count = 0
i_count = 0
counter = 0

for char in scores:
    if char == 'C':
        c_count += 1
    elif char == 'I':
        i_count += 1
    if i_count == 3:
        break

if i_count == 3:
    print("Game over")
else:
    print("You won")

print(c_count)
