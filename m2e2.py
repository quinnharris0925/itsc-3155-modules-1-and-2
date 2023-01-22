#detecting upper and lowercases; link: https://www.geeksforgeeks.org/isupper-islower-lower-upper-python-applications/
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