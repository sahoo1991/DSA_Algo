def pascal_triangle(n):
    result = [[1]]
    for i in range(1, n):
        prev = result[-1]
        current = [1]
        for j in range(len(prev)-1):
            current.append(prev[j] + prev[j+1])
        current.append(1)
        result.append(current)
    for item in result:
        print(item)
    return result

def get_pascal_triangle_value(n, r):
    n = n-1
    r = r-1
    if r > n-r:
        r = n-r
    result = 1
    for i in range(r):
        result *= n - i
        result //= i +1
    return result






n = 5
result = pascal_triangle(n)
print(get_pascal_triangle_value(4,4))
