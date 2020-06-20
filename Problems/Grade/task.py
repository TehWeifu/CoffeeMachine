grade = int(input())
max_grade = int(input())

if grade >= max_grade * 0.9:
    print('A')
elif grade >= max_grade * 0.8:
    print('B')
elif grade >= max_grade * 0.7:
    print('C')
elif grade >= max_grade * 0.6:
    print('D')
else:
    print('F')
