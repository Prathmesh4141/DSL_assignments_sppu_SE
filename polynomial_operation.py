def add(A, B, m, n):
    sum = []

    
    for i in range(m+1):
        sum.append(A[i])

    for i in range(n+1):
        sum[i] += B[i]

    return sum

def multiply(A, B, m, n):
    sum1 = []

    
    for i in range(m+1):
        sum1.append(A[i])

    for i in range(n+1):
        sum1[i] *= B[i]

    return sum1

def printPoly(poly, n):
    for i in range(n):
        print(poly[i], end = "")
        if (i != 0):
            print("x^", i, end = "")
        if (i != n - 1):
            print(" + ", end = "")
    
    "\n"


    
m=int(input("enter the degree of 1st polynomial: "))
A=[]
for i in range (0,m+1):
    k=int(input(f"enter the coefficient of x^{i}: "))
    A.append(k)

n=int(input("enter the degree of 2st polynomial: "))
B=[]

for i in range (0,n+1):
    k=int(input(f"enter the coefficient of x^{i}: "))
    B.append(k)




print("First polynomial is: ")
printPoly(A, m+1)

print("\n", end = "")

print("Second polynomial is")
printPoly(B, n+1)

print("\n", end = "")

sum = add(A, B, m, n)
print("sum polynomial is")
printPoly(sum, n+1)

print("\n", end = "")

sum1=multiply(A,B,m,n)
print("multiplication of polynomial is")
printPoly(sum1, n+1)

