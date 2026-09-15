

# Input: nums = [-1,0,3,5,9,12], target = 9
#
# Output: 4
#
# Explanation: The target integer 9 exists in nums and its index is 4

def binary_search_iterative(nums, target):
    # TC: O(log n), SC: O(1)
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (right + left) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

def binary_search_recursive(nums, target, left, right):
    # TC: O(log n), SC: O(log n)
    if left > right:
        return -1

    mid = (right + left) // 2

    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        return binary_search_recursive(nums, target, mid + 1, right)
    else:
        return binary_search_recursive(nums, target, left, mid - 1)






nums = [-1,0,3,5,9,12]
target = 9

print(binary_search_iterative(nums, target))
print(binary_search_recursive(nums, target, 0, len(nums) - 1))