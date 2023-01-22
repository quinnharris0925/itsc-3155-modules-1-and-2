#detecting upper and lowercases; link: https://www.geeksforgeeks.org/isupper-islower-lower-upper-python-applications/
#Joining lists of strings; Link: https://note.nkmk.me/en/python-string-concat/#:~:text=You%20can%20concatenate%20a%20list,the%20string%20method%2C%20join()%20.&text=Call%20the%20join()%20method,pass%20%5BList%20of%20strings%5D%20.&text=If%20you%20use%20an%20empty,makes%20a%20comma%2Ddelimited%20string.
inp = input("Enter a string: ")
l = 0
u = 0
lower = []
upper= []
out = ""
for c in inp:
    if c.islower() == True:
        lower.append(c)
    elif c.isupper() == True:
        upper.append(c)
for l in lower:
    out+=l
for u in upper:
    out+=u
print(out)