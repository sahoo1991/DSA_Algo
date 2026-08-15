# Input: nums = [7, 0, 0, 1, 7, 7, 2, 7, 7]
#
# Output: 7

def majority_element_boyer_moore_voting(nums):
    cur_elem = ""
    count = 0
    for num in nums:
        if count == 0:
            cur_elem = num
            count += 1
        elif num == cur_elem:
            count += 1
        else:
            count -= 1
    return cur_elem if nums.count(cur_elem) > len(nums)//2 else None

def majority_element_brute_1(nums):
    result = {}
    for num in nums:
        result[num] = result.get(num, 0) + 1
    for key, value in result.items():
        if value > len(nums) // 2:
            return key
    return None


def majority_element_brute(nums):
    ans = ''
    for i in range(len(nums)):
        count = 0
        for j in range(len(nums)):
            if i != j and nums[i] == nums[j]:
                count += 1
                if count > len(ans)// 2:
                    return nums[i]
    return None


nums = [-1, -1, -1, -1]
print(majority_element_boyer_moore_voting(nums))