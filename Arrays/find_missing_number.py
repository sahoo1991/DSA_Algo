
# Input: nums = [0, 2, 3, 1, 4]
#
# Output: 5
#
# Input: nums = [1, 3, 6, 4, 2, 5]
#
# Output: 0
#
# Input: nums = [0, 1, 2, 4, 5, 6]
#
# Output: 3

def find_missing_number_optimized(nums):
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum



def find_missing_number(nums):
    l = len(nums)
    nums.sort()
    if nums[0] != 0:
        return 0
    if nums[-1] != l:
        return l
    start = 1
    for i in range(1, l):
        if nums[i] != start:
            return i
        start += 1


nums = [0, 2, 3, 1, 4]
print(find_missing_number_optimized(nums))
