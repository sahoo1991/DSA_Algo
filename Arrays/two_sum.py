

# Input: nums = [1, 6, 2, 10, 3], target = 7
#
# Output: [0, 1]

def get_two_sum_indexes_brute(ls, target):
    for i in range(len(ls)):
        for j in range(i+1, len(ls)):
            if ls[i] + ls[j] == target:
                return i,j
    return None

def get_two_sum_optimized(ls, target):
    result = {}
    for index, value in enumerate(ls):
        if target - value in result:
            return result.get(target - value), index
        else:
            result[value] = index
    return None

def get_two_sum_optimal(ls, target):
    result = []
    for index, value in enumerate(ls):
        result.append([value, index])
    result.sort(key= lambda x : x[0])
    i , j = 0, len(ls) - 1
    while i < j:
        if result[i][0] + result[j][0] == target:
            return result[i][1], result[j][1]
        elif result[i][0] + result[j][0] < target:
            i+=1
        else:
            j -=1
    return -1, -1



# nums = [1, 6, 2, 10, 3]
# target = 7
nums = [1, 3, 5, -7, 6, -3]
target = 0
print(get_two_sum_optimal(nums, target))