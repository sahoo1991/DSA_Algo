# Input: nums = [4, 5, 3, 7, 1, 2]
#
# Output: 840
#
# Explanation:
#
# The largest product is given by the whole array itself

def max_product_subarray(nums):
    n = len(nums)
    prefix, suffix = 1, 1
    ans = float('-inf')
    for num in nums:
        prefix *= num
        suffix *= nums[n - 1 - nums.index(num)]
        if prefix == 0:
            prefix = 1
        if suffix == 0:
            suffix = 1
        ans = max(ans, max(prefix, suffix))

    return ans

# nums = [4, 5, 3, 7, 1, 2]
nums = [-5, 0, -2]
print(max_product_subarray(nums))