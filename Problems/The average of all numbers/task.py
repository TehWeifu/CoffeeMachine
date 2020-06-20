# put your python code here
a = int(input())
b = int(input())
vector_sum = 0
counter = 0

for num in range(a, b + 1, 1):
    if num % 3 == 0:
        vector_sum += num
        counter += 1

print(vector_sum / counter)
