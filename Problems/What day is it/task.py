current_time = (10.5 + float(input()))

if current_time < 0:
    print("Monday")
elif current_time > 24:
    print("Wednesday")
else:
    print("Tuesday")
