#Name-Prathmesh Dhole
#Roll no-7241
# batch-s4

#Check Upper Triangular Matrix
def is_upper_triangular(matrix):
    for i in range(len(matrix)):
        for j in range(i):
            if matrix[i][j] != 0:
                return False
    return True

#Diagonal sum
def diagonal_sum(matrix):
    sum=0
    for i in range (len(matrix)):
        sum+=matrix[i][i]
    return sum



#transpose of matrix
def transpose(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

#adddition of matrix
def add_matrices(matrix1, matrix2):
    return [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]


#multiplication of matrix
def multiply_matrices(matrix1, matrix2):
    result = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result


#saddle point
def saddle_point(matrix):
    for i in range(len(matrix)):
        row_min = min(matrix[i])
        col_index = matrix[i].index(row_min)
        col_max = max(matrix[j][col_index] for j in range(len(matrix)))
        if row_min == col_max:
            return (i, col_index)
    return None

#magic square
def is_magic_square(matrix):
    n = len(matrix)
    s = n * (n * n + 1) // 2
    for row in matrix:
        if sum(row) != s:
            return False
    for col in range(n):
        if sum(matrix[row][col] for row in range(n)) != s:
            return False
    if sum(matrix[i][i] for i in range(n)) != s:
        return False
    if sum(matrix[i][n - 1 - i] for i in range(n)) != s:
        return False
    return True

#---------------------------------------inputs---------------------------------------------
#Matrix 1 input
rows1 = int(input("Enter number of rows1: "))
cols1 = int(input("Enter number of columns1: "))

matrix1 = []
for i in range(rows1):
    row = []
    for j in range(cols1):
        element = int(input(f"Enter element at position [{i}][{j}]: "))
        row.append(element)
    matrix1.append(row)




#Matrix 2 input
rows2 = int(input("Enter number of rows2: "))
cols2 = int(input("Enter number of columns2: "))

matrix2 = []
for i in range(rows2):
    row = []
    for j in range(cols2):
        element = int(input(f"Enter element at position [{i}][{j}]: "))
        row.append(element)
    matrix2.append(row)




# ---------------------------------------outputs---------------------------------------------

print("matrix1 Is upper triangular:", is_upper_triangular(matrix1))
print("matrix2 Is upper triangular:", is_upper_triangular(matrix2))
print("Diagonal sum of matrix1:", diagonal_sum(matrix1))
print("Diagonal sum of matrix2:", diagonal_sum(matrix2))
print("Transpose:")
for row in transpose(matrix1):
    print(row)
print("Addition of matrices:")
for row in add_matrices(matrix1, matrix2):
    print(row)
print("Multiplication of matrices:")
for row in multiply_matrices(matrix1, matrix2):
    print(row)
print("Saddle point:", saddle_point(matrix2))
print("Is magic square:", is_magic_square(matrix2))
