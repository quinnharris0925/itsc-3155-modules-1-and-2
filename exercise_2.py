#Comparing Strings fuctions and syntax; Link:https://note.nkmk.me/en/python-str-compare/
#Worked with Lenny Volpe
s1 = input('Enter first string: ')
s2 = input('Enter second string: ')
b1 = s1.endswith(s2)
b2 = s2.endswith(s1)
b3 = False
if b1 or b2 == True:
    b3 = True
print(b3)
