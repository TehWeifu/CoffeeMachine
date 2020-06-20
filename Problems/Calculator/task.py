# put your python code here
num1 = float(input())
num2 = float(input())
operator = input()

if operator == '+':
    print(num1 + num2)
elif operator == '-':
    print((num1 - num2))
elif operator == '/':
    if num2 == 0:
        print("Division by 0!")
    else:
        print(num1 / num2)
elif operator == '*':
    print(num1 * num2)
elif operator == "mod":
    if num2 == 0:
        print("Division by 0!")
    else:
        print(num1 % num2)
elif operator == "pow":
    print(num1 ** num2)
elif operator == "div":
    if num2 == 0:
        print("Division by 0!")
    else:
        print(num1 // num2)
