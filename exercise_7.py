#Detecting even numbers; Link: https://www.geeksforgeeks.org/python-program-to-print-even-numbers-in-a-list/
#Worked with Lenny Volpe
l = []
e = []
i = 0
while i == 0:
    inp = input('Enter a number or QUIT to quit: ')
    if inp == 'QUIT':
        i = 1
    else:
        l.append(int(inp))
print("Full list:", end=" ")
print(l)
for num in l:
    if num % 2 == 0:
        e.append(num)
print("Even numbers: ", end='')
print(e)

