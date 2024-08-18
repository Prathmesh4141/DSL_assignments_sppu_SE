# Bolo Jai shree ram

# Linear Search

def linear_search(a, x):
    for i in range(len(a)):

        if a[i] == x:
            return i

    return -1


# Sentinel Search

def sentinel_search(a, x):
    count = len(a)
    a.append(x)
    i = 0

    while a[i] != x:
        i = i + 1

    if i != count:
        return i
    else:
        return -1



def binary_search(a, l, r, x):
    a.sort()
    while l <= r:

        mid = l + (r - l) // 2;

        if a[mid] == x:
            return mid

        elif a[mid] < x:
            l = mid + 1

        else:
            r = mid - 1

    return -1


# Fibonacci Search

def fibonacci_search(a, x):
    a.sort()
    fib1, fib2 = 1, 0
    fibn = fib2 + fib1
    a_len = len(a)
    while fibn < a_len:
        fib2 = fib1
        fib1 = fibn
        fibn = fib2 + fib1
    ind = -1
    while fibn > 1:
        n = min(ind + fib2, a_len - 1)
        if a[n] > x:
            fibn = fib2
            fib1 = fib1 - fib2
            fib2 = fibn - fib1
        elif a[n] < x:
            fibn = fib1
            fib1 = fib2
            fib2 = fibn - fib1
            ind = n
        else:
            return n
    if a[ind + 1] == n and fib1 == 1:
        return ind + 1
    return -1




no_stud = int(input("Enter the number of Students : "))
a = []
for i in range(0, no_stud):
    a.append(int(input("Enter the Roll Number : ")))

roll = int(input("Enter the Roll Number to be search : "))


a1 =a.copy()
a1.sort()

print()
index = linear_search(a, roll)
print("using linear search")
if index != -1:
    print("Roll number", roll, " at the index", index, "has Attended the training program ")
else:
    print("Roll number", roll, "has not Attended the training program")


print()

print("using sentinel search")
index1 = sentinel_search(a, roll)
if index1 == -1:
    print("Roll number", roll, "has not Attended the training program")
else:
    print("Roll number", roll, " at the index", index1, "has Attended the training program")


print()

print("using binary search")
index2 = binary_search(a1, 0, len(a) - 1, roll)
if index2 == -1:
    print("Roll number", roll, "has not Attended the training program")
else:
    print("Roll number", roll, " at the index", index2, "has Attended the training program")


print()

print("using fibonacci search")
index3 = fibonacci_search(a1, roll)
if index3== -1:
        print("Roll number", roll, "has not Attended the training program")
else:
    print("Roll number", roll, " at the index", index3, "has Attended the training program")
