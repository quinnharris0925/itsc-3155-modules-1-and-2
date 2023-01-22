inp = input("Enter a string: ")
keys = []
dict = {}
for i in inp:
    if i not in keys:
        keys.append(i)
        dict[i] = 1
    else:
        dict[i] += 1
print(dict)