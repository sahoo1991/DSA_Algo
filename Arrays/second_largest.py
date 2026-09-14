def second_large(ls):
    if len(ls) == 1:
        return ls[0]
    first, second = float('-inf'), float('-inf')
    for item in ls:
        if item > first:
            second = first
            first = item
        elif item > second and item != first:
            second = item
    if second == float('-inf'):
        second = -1
    return second



ls =   [7, 7, 2, 2, 10, 10, 10]
print(second_large(ls))

# TC - O(n) - The function iterates through the list once, where n is the number of elements in the list.
# SC - O(1) - The function uses a constant amount of space regardless of the