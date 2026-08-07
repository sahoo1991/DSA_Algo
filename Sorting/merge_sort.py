def merge_two_sorted_list(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    if i < len(left):
        while i < len(left):
            result.append(left[i])
            i += 1
    if j < len(right):
        while j < len(right):
            result.append(right[j])
            j += 1
    return result


def merge_sort(ls):
    if len(ls) <= 1:
        return ls
    mid = len(ls) // 2
    left_arr = ls[:mid]
    right_arr = ls[mid:]
    l_sorted = merge_sort(left_arr)
    r_sorted = merge_sort(right_arr)
    return merge_two_sorted_list(l_sorted, r_sorted)


ls = [7, 4, 1, 5, 3]
print(merge_sort(ls))
print(ls)
