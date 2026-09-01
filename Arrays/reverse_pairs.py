# Input: nums = [6, 4, 1, 2, 7]
#
# Output: 3
#
# Explanation:
#
# The reverse pairs are:
#
# (0, 2) : nums[0] = 6, nums[2] = 1, 6 > 2 * 1
#
# (0, 3) : nums[0] = 6, nums[3] = 2, 6 > 2 * 2
#
# (1, 2) : nums[1] = 4, nums[2] = 1, 4 > 2 * 1

def merge_two_sorted_list(left, right):
    # Count reverse pairs FIRST (before merging)
    count = 0
    j = 0
    for i in range(len(left)):
        while j < len(right) and left[i] > 2 * right[j]:
            j += 1
        count += j
    
    # Now merge normally
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
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



nums = [6, 4, 1, 2, 7]
print(merge_sort(nums))