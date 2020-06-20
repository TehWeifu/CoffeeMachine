# put your python code here
number = int(input())
regular_sum = number
squared_sum = number * number

while regular_sum != 0:
    number = int(input())
    regular_sum += number
    squared_sum += number * number

print(squared_sum)
