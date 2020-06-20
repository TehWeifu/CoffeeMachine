class RightTriangle:
    def __init__(self, hyp, leg_1, leg_2):
        self.c = hyp
        self.a = leg_1
        self.b = leg_2
        # calculate the area here
        self.s = float(1 / 2 * leg_1 * leg_2)


# triangle from the input
input_c, input_a, input_b = [int(x) for x in input().split()]

# write your code here
test = RightTriangle(input_c, input_a, input_b)

if test.c ** 2 == test.b ** 2 + test.a ** 2:
    print("%.1f" % float(test.s))
else:
    print("Not right")
