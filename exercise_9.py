#Worked with Lenny Volpe
words = []
for i in range(5):
    words.append(input('Enter a word: '))
print(words)
w = ""
for word in words:
    w = w + " " + word
print(w)