# bubble sort
def bubble_sort(roll):
    print("Original array is ", roll)
    for i in range(len(roll)-1):
        for j in range(len(roll)-i-1):
            if roll[j] > roll[j+1]:
                roll[j],roll[j+1] = roll[j+1],roll[j]
        print("Pass " + str(i+1) + ":", roll)
    return roll


n = int(input("Enter the length of list- "))
roll = []
for i in range(n):
    element = int(input("Enter the "+str(i+1)+"st number-\n"))
    if element > 0:
        roll.append(element)

bubble_sort(roll)

print("The rolls of the students after sorting are-", roll)
