# Input: nums = [1, 2, 5, 3, 1, 2]
#
# Output: [5, 3, 2]

def leaders_in_array(ls):
    result = []
    current_leader = ls[-1]
    result.append(ls[-1])
    for i in range(len(nums) -2, -1, -1):
        if nums[i] > current_leader:
            result.append(nums[i])
            current_leader = nums[i]
    return result[::-1] if len(result) > 0 else None



nums = [1, 2, 5, 3, 1, 2]
# nums =  [-3, 4, 5, 1, -4, -5]
# nums = [-3, 4, 5, 1, -30, -10]
print(leaders_in_array(nums))