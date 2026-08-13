

# Input: nums = [0, 0, 3, 3, 5, 6]
#
# Output: 4

def remove_duplicates(nums):
    result = []
    for num in nums:
        if num not in result:
            result.append(num)
    return result


def remove_duplicates_in_space(nums):
    start = 0
    count = 0
    for j in range(1, len(nums)):
        if nums[j] != nums[start]:
            nums[start+1] = nums[j]
            count += 1
            start += 1
    return count + 1


nums = [0, 0, 3, 3, 5, 6]
print(remove_duplicates_in_space(nums))
print(nums)
