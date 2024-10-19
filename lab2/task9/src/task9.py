import time
start = time.perf_counter()
def split(matrix):
    n = len(matrix)
    mid = n // 2

    A11 = [[matrix[i][j] for j in range(mid)] for i in range(mid)]
    A12 = [[matrix[i][j] for j in range(mid, n)] for i in range(mid)]
    A21 = [[matrix[i][j] for j in range(mid)] for i in range(mid, n)]
    A22 = [[matrix[i][j] for j in range(mid, n)] for i in range(mid, n)]

    return A11, A12, A21, A22

def add(A, B):
    n = len(A)
    return [[A[i][j] + B[i][j] for j in range(n)] for i in range(n)]

def sub(A, B):
    n = len(A)
    return [[A[i][j] - B[i][j] for j in range(n)] for i in range(n)]

def strassen(A, B):
    n = len(A)

    if n == 1:
        return [[A[0][0] * B[0][0]]]

    A11, A12, A21, A22 = split(A)
    B11, B12, B21, B22 = split(B)

    P1 = strassen(A11, sub(B12, B22))
    P2 = strassen(add(A11, A12), B22)
    P3 = strassen(add(A21, A22), B11)
    P4 = strassen(A22, sub(B21, B11))
    P5 = strassen(add(A11, A22), add(B11, B22))
    P6 = strassen(sub(A12, A22), add(B21, B22))
    P7 = strassen(sub(A11, A21), add(B11, B12))

    C11 = add(sub(add(P5, P4), P2), P6)
    C12 = add(P1, P2)
    C21 = add(P3, P4)
    C22 = sub(sub(add(P5, P1), P3), P7)

    new_matrix = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n // 2):
        for j in range(n // 2):
            new_matrix[i][j] = C11[i][j]
            new_matrix[i][j + n // 2] = C12[i][j]
            new_matrix[i + n // 2][j] = C21[i][j]
            new_matrix[i + n // 2][j + n // 2] = C22[i][j]

    return new_matrix


with open('../tests/input.txt', 'r') as file:
    n = int(file.readline().strip())

    A = []
    for _ in range(n):
        row = list(map(int, file.readline().strip().split()))
        A.append(row)

    B = []
    for _ in range(n):
        row = list(map(int, file.readline().strip().split()))
        B.append(row)
C = strassen(A, B)

with open('../tests/output.txt', 'w') as file:
    for row in C:
        file.write(' '.join(map(str, row)) + '\n')

stop = time.perf_counter()
print("time:", (stop - start))