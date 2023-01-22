def ulist(list):
    ulist = []
    for n in list:
        if n not in ulist:
            ulist.append(n)
    return ulist
my_list = [1, 2, 3, 4, 5, 2, 1, 6]
new_list = ulist(my_list)
print(new_list)