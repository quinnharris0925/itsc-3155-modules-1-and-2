#Range Function & For loops syntax; Link:https://www.w3schools.com/python/python_for_loops.asp
#Worked with Lenny Volpe
num = input('Enter an integer greater than 1: ')
num = int(num)
for x in range(num + 1):
    print('The cube of ' + str(x) + ' is ' + str(x**3))