#print on the same line with the end parameter; Link: https://www.tutorialspoint.com/how-to-print-in-same-line-in-python
#Worked with Lenny Volpe
row = int(input('Enter a row number from 1 to 5: '))
col = int(input('Enter a column number from 1 to 5: '))

for r in range(1, 6):
    for c in range(1,6):
        if r == row and c == col:
            print('1', end=' ')
        else:
            print('0', end=' ')
    print()
