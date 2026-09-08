











# Input: nums = [100, 4, 200, 1, 3, 2]
#
# Output: 4

def longestConsecutive(nums):
    nums.sort()
    print(nums)
    unique = {num : True for num in nums}
    count = 1
    max_count = 1
    data = list(unique.keys())
    print(data)
    for i in range(len(data) - 1):
        if data[i] + 1 == data[i + 1]:
            count += 1
            max_count = max(max_count, count)
        else:
            count = 1
    return max_count

def longest_consecutive_optimal(nums):
    num_set = set(nums)
    max_count = 0

    for num in num_set:
        if num - 1 not in num_set:
            current_num = num
            current_count = 1

            while current_num + 1 in num_set:
                current_num += 1
                current_count += 1

            max_count = max(max_count, current_count)

    return max_count





# nums = [100, 4, 200, 1, 3, 2]
nums = [-19,-9,15,2,7,16,11,-16,2,13,-8,2,1,16,18,-5,-13,-14,-9,-2,9,12,7,-1,15,-6,3,-9]
print(longestConsecutive(nums))
print(longest_consecutive_optimal(nums))