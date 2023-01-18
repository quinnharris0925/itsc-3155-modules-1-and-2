#List syntax and append function; Link: https://www.pythoncentral.io/lists-in-python-how-to-create-a-list-in-python/#:~:text=To%20define%20lists%20in%20Python,items%20between%20two%20square%20brackets.&text=The%202nd%20method%20is%20to,passing%20the%20items%20to%20it.&text=The%20list%20can%20accept%20any%20data%20type.
#Worked with Lenny Volpe
x = input("How many numbers would you like to list? ")
x =  int(x)
i = 0
items = []
while i<x:
    num = input("Enter number " +str(i+1)+ ": ")
    num = float(num)
    items.append(num)
    i= i+1
print(items)