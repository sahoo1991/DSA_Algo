# Input: nums = [2, 3, 7, 1, 3, 5]
#
# Output: 5
#
# Explanation:
#
# The responsible indexes are:
#
# nums[0], nums[3], values: 2 > 1 & indexes: 0 < 3
#
# nums[1], nums[3], values: 3 > 1 & indexes: 1 < 3
#
# nums[2], nums[3], values: 7 > 1 & indexes: 2 < 3
#
# nums[2], nums[4], values: 7 > 3 & indexes: 2 < 4
#
# nums[2], nums[5], values: 7 > 5 & indexes: 2 < 5

def merge_two_sorted_list(left, right):
    result = []
    i, j = 0, 0
    count = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            count += len(left) - i
            j += 1
    if i < len(left):
        while i < len(left):
            result.append(left[i])
            i += 1
    if j < len(right):
        while j < len(right):
            result.append(right[j])
            j += 1
    return result, count


def merge_sort(ls):
    count = 0
    if len(ls) <= 1:
        return ls, count
    mid = len(ls) // 2
    left_arr = ls[:mid]
    right_arr = ls[mid:]
    l_sorted, l_count = merge_sort(left_arr)
    r_sorted, r_count = merge_sort(right_arr)
    merged, merge_count = merge_two_sorted_list(l_sorted, r_sorted)
    count = l_count + r_count + merge_count
    return merged, count



nums = [2, 3, 7, 1, 3, 5]
print(merge_sort(nums))