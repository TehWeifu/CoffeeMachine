letters = list("qwertyuiopasdfghjklzxcvbnm")
vowels = list("aeiou")
word = input()
counter = 0

for letter in word:
    if letter in letters:
        if letter in vowels:
            print("vowel")
        else:
            print("consonant")
    else:
        break
