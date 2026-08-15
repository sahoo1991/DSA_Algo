# Input : nums = [2, 4, 5, -1, -3, -4]
#
# Output : [2, -1, 4, -3, 5, -4]

def rearrange_by_sign(nums):
    result = [0] * len(nums)
    pos_sign = 0
    neg_sign = 1
    for num in nums:
        if num > 0:
            result[pos_sign] = num
            pos_sign += 2
        else:
            result[neg_sign] = num
            neg_sign += 2
    return result



# nums = [2, 4, 5, -1, -3, -4]
# nums = [1, -1, -3, -4, 2, 3]
nums = [-4, 4, -4, 4, -4, 4]
print(rearrange_by_sign(nums))