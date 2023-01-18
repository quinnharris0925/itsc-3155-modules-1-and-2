#String to 'char' List, ; Link:https://www.geeksforgeeks.org/python-program-convert-string-list/
#Worked with Lenny Volpe
w = input( 'enter a string: ')
l = list(w)
l2 = []
print(w)

for x in range(0, len(l), 3):
    l3 = []
    for y in range(3):
        z = x + y
        if z < len(l):
            l3.append(l[z])
    l2.append(l3)

print(l)
print(l2)