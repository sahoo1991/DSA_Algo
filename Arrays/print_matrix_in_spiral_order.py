# Input: matrix = [[1, 2, 3], [4 ,5 ,6], [7, 8, 9]]
#
# Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]
def get_spiral_matrix(ls):
    result = []
    top, left = 0, 0
    bottom, right = len(ls) -1, len(ls[0]) -1
    while top <= bottom and left <= right:
        for i in range(left, right +1):
            result.append(ls[top][i])
        top += 1
        for j in range(top, bottom + 1):
            result.append(ls[j][right])
        right -= 1
        if top <= bottom:
            for k in range(right, left -1, -1):
                result.append(ls[bottom][k])
            bottom -= 1
        if left <= right:
            for m in range(bottom, top -1, -1):
                result.append(ls[m][left])
            left += 1
    return result


# matrix = [[1, 2, 3], [4 ,5 ,6], [7, 8, 9]]

# matrix = [[1, 2, 3],
#           [4 ,5 ,6],
#           [7, 8, 9]]

# matrix = [[1, 2, 3, 4], [5, 6, 7, 8]]

matrix = [[1, 2], [3, 4], [5, 6], [7, 8]]
print(get_spiral_matrix(matrix))