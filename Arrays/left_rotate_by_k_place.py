# Input: nums = [1, 2, 3, 4, 5, 6], k = 2
# 2,1,6,5,4,3
#
# Output: nums = [3, 4, 5, 6, 1, 2]

def reverse(nums, low, high):
    start = low
    end = high
    while start < end:
        temp = nums[start]
        nums[start] = nums[end]
        nums[end] = temp
        start += 1
        end -= 1



def left_rotate_by_k(nums, k):
    if k > len(nums):
        k = len(nums) % k
    temp = []
    for m in range(k):
        temp.append(nums[m])
    for i in range(k, len(nums)):
        nums[i - k] = nums[i]
    start = 0
    for j in range(len(nums) - k, len(nums)):
        nums[j] = temp[start]
        start += 1

def left_rotate_by_k_optimized(nums, k):
    if k > len(nums):
        k = len(nums) % k
    reverse(nums, 0, k-1)
    reverse(nums, k, len(nums)-1)
    reverse(nums, 0, len(nums)-1)




nums = [1, 2, 3, 4, 5, 6]
left_rotate_by_k_optimized(nums, 2)
print(nums)