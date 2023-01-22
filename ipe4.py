#isDigit method for integer detection; Link: https://favtutor.com/blogs/check-string-is-integer-python#:~:text=The%20isdigit()%20method%20is,and%20False%20if%20it's%20not.
count = 1
s = 0
while count < 6:
    inp = input('Enter int #' + str(count) + ": ")
    if inp.isdigit() == True:
        s = s + int(inp)
        count+=1
    else:
        print("Invalid input. Please enter an int.")
print("Your sum is " + str(s))