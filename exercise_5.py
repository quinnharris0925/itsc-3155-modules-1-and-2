#not in function; Link:https://www.dataquest.io/blog/how-to-remove-duplicates-from-a-python-list/
#Worked with Lenny Volpe
x=0
l1 = []
l2 =[]
l3 = []
while x < 5:
    num = int(input('Enter a numer for the first list: '))
    l1.append(num)
    x=x+1
x=0
while x < 5:
    num = int(input('Enter a numer for the second list: '))
    l2.append(num)
    x=x+1
for num in l1:
    if num not in l3:
        l3.append(num)
for num in l2:
    if num not in l3:
        l3.append(num)
print("First list: " + str(l1))
print('Second list: ' + str(l2))
print('Third list: ' + str(l3))