axis_x = float(input())
axis_y = float(input())

if axis_x > 0:
    if axis_y > 0:
        print("I")
    else:
        print("IV")
else:
    if axis_y > 0:
        print("II")
    else:
        print("III")
