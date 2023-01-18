#If statement syntax; Link:https://www.w3schools.com/python/python_conditions.asp
#Worked with Lenny Volpe
grade = input('What was your final numerical grade?')
grade = int(grade)
if grade > 89:
    print('Letter Grade: A')
elif grade > 79:
    print('Letter Grade: B')
elif grade > 69:
    print('Letter Grade: C')
elif grade > 59:
    print('Letter Grade: D')
else:
    print('Letter Grade: F')

