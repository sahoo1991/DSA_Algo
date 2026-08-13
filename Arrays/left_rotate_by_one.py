

# Input: nums = [1, 2, 3, 4, 5]
#
# Output: [2, 3, 4, 5, 1]

def left_rotate_by_one(nums):
    if len(nums) > 1:
        first = nums[0]
        for i in range(1, len(nums)):
            nums[i-1] = nums[i]
        nums[-1] = first

# nums = [1, 2, 3, 4, 5]
# nums = [-1, 0, 3, 6]
nums = [7, 6, 5, 4]
left_rotate_by_one(nums)
print(nums)