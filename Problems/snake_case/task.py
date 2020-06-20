string = input()
result = ""

for char in string:
    if char == char.upper():
        result += '_'
        result += char.lower()
    else:
        result += char

print(result)
