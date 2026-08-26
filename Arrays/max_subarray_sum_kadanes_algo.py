# Input: nums = [2, 3, 5, -2, 7, -4]
#
# Output: 15

def max_sub_array_optimal(ls):

    max_sum = float('-inf')
    temp_sum = 0
    start_ind, end_ind = -1, -1
    start = -1
    for index , num in enumerate(ls):
        if temp_sum == 0:
            start = index
        temp_sum += num
        if temp_sum > max_sum:
            start_ind = start
            end_ind = index
            max_sum = temp_sum
        if temp_sum < 0:
            temp_sum = 0
    print(start_ind, end_ind)
    return max_sum


def max_sub_array_sum(ls):
    max_result = float('-inf')

    for i in range(len(ls)):
        sum = 0
        # for j in range(i, len(ls)):
        #     sum = 0
        #     for k in range(i, j+1):
        #         sum += ls[k]
        #     max_result = max(max_result, sum)
        for j in range(i, len(ls)):
            sum += ls[j]
            max_result = max(max_result, sum)

    return max_result


nums = [2, 3, 5, -2, 7, -4]
print(max_sub_array_optimal(nums))