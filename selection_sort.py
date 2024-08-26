# selection sort
def selection_sort(roll):
    print("Original array is ", roll)
    for i in range(len(roll)-1):
        min = i
        for j in range(i+1, len(roll), 1):
            if (roll[j] < roll[min]):
                min = j
        roll[i],roll[min] = roll[min],roll[i]
        print("Pass " + str(i+1) + ":" , roll)
    return roll


n = int(input("Enter the number of students here- "))
roll = []
for i in range(n):
    element = int(input("Enter the "+str(i+1)+"st number-\n"))
    if element > 0:
        roll.append(element)

selection_sort(roll)

print("The rolls of the students after sorting are-", roll)
