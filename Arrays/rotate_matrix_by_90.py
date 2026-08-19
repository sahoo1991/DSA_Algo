
# Input: matrix = [[1, 1, 2], [5, 3, 1], [5, 3, 5]]
#
# Output:
#
# [[5, 5, 1], [3, 3, 1], [5, 1, 2]]

def rotate_matrix_by_90_brute(matrix):
    n = len(matrix)
    m = len(matrix[0])
    for i in range(m):
        temp = []
        for j in range(n):
            temp.append(matrix[j][i])
        temp.reverse()
        print(temp)


def rotate_matrix_by_90_brute_2(matrix):
    n = len(matrix)
    temp = [[0] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            temp[j][n - 1 - i] = matrix[i][j]
    for i in range(n):
        matrix[i] = temp[i]

def rotate_matrix_90_optimized(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i):
            matrix[i][j] , matrix[j][i] = matrix[j][i], matrix[i][j]
    for i in range(n):
        for j in range(n // 2):
            matrix[i][j], matrix[i][n-j-1] = matrix[i][n-j-1], matrix[i][j]




matrix = [[1, 1, 2],
          [5, 3, 1],
          [5, 3, 5]]


rotate_matrix_90_optimized(matrix)
print(matrix)