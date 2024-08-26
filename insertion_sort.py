# insertion sort
def insertion_sort(roll):
    for i in range(len(roll)):
        key = roll[i]
        j = i - 1
        while (j >= 0 and key < roll[j]):
            roll[j+1] = roll[j]
            j = j - 1
        roll[j+1] = key
        print("Pass " + str(i+1) + ":", roll)
    return roll





n = int(input("Enter the number of students here- "))
roll = []
for i in range(n):
    element = int(input("Enter the "+str(i+1)+"st number-\n"))
    if element > 0:
        roll.append(element)

insertion_sort(roll)

print("The rolls of the students after sorting are-", roll)

