




# Input: nums = [0, 1, 4, 0, 5, 2]
#
# Output: [1, 4, 5, 2, 0, 0]

def move_zeroes_inplace(nums):
    start = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            start = i
            break
    for j in range(start, len(nums)):
        if nums[j] != 0:
            nums[start], nums[j] = nums[j], nums[start]
            start += 1


def move_zeroes(nums):
    result = []
    count = []
    for i in range(len(nums)):
        if nums[i] != 0:
            result.append(nums[i])
        else:
            count.append(0)
    result.extend(count)
    return result


nums = [0, 1, 4, 0, 5, 2]
# print(move_zeroes(nums))
# print(nums)
print(move_zeroes_inplace(nums))
print(nums)
