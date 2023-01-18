#Count function, Link:https://www.w3schools.com/python/ref_list_count.asp
#Worked with Lenny Volpe
nums = []
unis = []

for i in range(10):
    inp = int(input("Enter number " + str(i+1) + ": "))
    nums.append(inp)
for num in nums:
    if nums.count(num) == 1:
        unis.append(num)

print("Full list: " + str(nums))
print("Nums that appear once: " + str(unis))