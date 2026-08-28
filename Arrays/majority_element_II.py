# Input: nums = [1, 2, 1, 1, 3, 2]
#
# Output: [1]

def majority_element_better(ls):
    result = {}
    ans = []
    for num in ls:
        result[num] = result.get(num, 0) + 1
    for key, value in result.items():
        if value > len(ls) // 3:
            ans.append(key)
    return ans

def majority_element_brute(ls):
    result = []
    for i in range(len(ls)):
        count = 1
        for j in range(len(ls)):
            if i != j and ls[i] == ls[j]:
                count += 1
        if count > len(ls) // 3:
            if len(result) == 0:
                result.append(ls[i])
            elif result[0] != ls[i]:
                result.append(ls[i])
        if len(result) == 2:
            break
    return result

def majority_element_boyer_moore_voting_extended(ls):
    cnt1, cnt2 = 0, 0
    el1, el2 = None, None

    for num in ls:
        if num == el1:
            cnt1 += 1
        elif num == el2:
            cnt2 += 1
        elif cnt1 == 0:
            cnt1 = 1
            el1 = num
        elif cnt2 == 0:
            cnt2 = 1
            el2 = num
        else:
            cnt2 -= 1
            cnt1 -= 1
    return el1, el2



nums = [1, 2, 1, 1, 3, 2]
# nums = [1, 2, 1, 1, 3, 2, 2]
# nums = [1, 2, 1, 1, 3, 2, 2, 3]
print(majority_element_brute(nums))