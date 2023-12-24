A = [[4, 6, 7],
     [4, 5, 2],
     [7, 8, 4]]
B = [[1, 1, 2],
     [3, 8, 1],
     [1, 6, 1]]
C = []
for i in range(len(A)):
    row = []
    for j in range(len(A[0])):
        row.append(A[i][j] + B[i][j])
    C.append(row)
print(C)