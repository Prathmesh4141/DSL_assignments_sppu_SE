def shell_sort(roll,size):
    interval = size // 2
    while interval > 0:
        for i in range(interval,size):
            temp = roll[i]
            j = i
            while j >= interval and roll[j - interval] > temp:
                roll[j] = roll[j - interval]
                j -= interval
            roll[j] = temp
        interval = interval // 2
        



n = int(input("Enter the number of students here- "))
roll = []
for i in range(n):
    element = int(input("Enter the "+str(i+1)+"st number-\n"))
    if element > 0:
        roll.append(element)

shell_sort(roll,n)
print("The rolls of the students after sorting are-", roll)

