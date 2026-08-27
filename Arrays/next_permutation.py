# Input: nums = [1,2,3]
#
# Output: [1,3,2]

def get_next_permutation(ls):
    ind = -1

    for i in range(len(ls) - 2, -1, -1):
        if ls[i] < ls[i+1]:
            ind = i
            break
    if ind == -1:
        ls.reverse()
        return
    for i in range(len(ls) - 1, ind, -1):
        if ls[i] > ls[ind]:
            ls[ind], ls[i] = ls[i], ls[ind]
            break
    start = ind + 1
    end = len(ls) - 1
    while start < end:
        ls[start], ls[end] = ls[end], ls[start]
        start += 1
        end -= 1
    return



# nums = [1,2,3]
# nums = [3,2,1]
# nums = [1,1,5]
nums = [2,1,5,4,3,0,0]
get_next_permutation(nums)
print(nums)