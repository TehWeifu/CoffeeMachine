# put your python code here
word = input()

for i in range(0, round(len(word) / 2)):
    if word[i] != word[len(word) - i - 1]:
        print("Not palindrome")
        break
else:
    print("Palindrome")
