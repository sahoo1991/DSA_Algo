# Input : n= 4, nums = [1,2,2,3], x = 2
#
# Output:3
#
# Explanation:
#
# Index 3 is the smallest index such that arr[3] > x.

def upper_bound_index(nums, x):
    # TC: O(n), SC: O(1)
    for i in range(len(nums)):
        if nums[i] > x:
            return i
    return len(nums)

def upper_bound(nums, x):
    # TC: O(log n), SC: O(1)
    left, right = 0, len(nums) - 1
    ans = len(nums)
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] > x:
            ans = mid
            right = mid - 1
        else:
            left = mid + 1
    return ans


nums = [1,2,2,3]
x = 2
print(upper_bound_index(nums, x))  # Output: 3
print(upper_bound(nums, x))  # Output: 3
