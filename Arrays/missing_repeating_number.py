# Input: nums = [3, 5, 4, 1, 1]
#
# Output: [1, 2]

def missing_repeating_brute(ls):
    missing = None
    repeat = None
    for i in range(1, len(ls) + 1):
        if i not in ls:
            missing = i
            break
    for num in ls:
        count = 0
        for num1 in ls:
            if num == num1:
                count += 1
        if count == 2:
            repeat = num
            break

    return repeat, missing


def missing_repeating_optimal(nums):
    sum_num, sum_sqr = 0, 0
    n = len(nums)
    for num in nums:
        sum_num += num
        sum_sqr += num * num
    act_sum = (n * (n + 1)) // 2
    act_sqr_sum = (n * (n + 1) * (2 * n + 1)) // 6
    val1 = sum_num - act_sum
    val2 = sum_sqr - act_sqr_sum
    val2 = val2 // val1
    missing = (val1 + val2) // 2
    repeating = missing - val1
    return missing, repeating




# nums = [3, 5, 4, 1, 1]
# nums = [1, 2, 3, 6, 7, 5, 7]
nums = [6, 5, 7, 1, 8, 6, 4, 3, 2]
print(missing_repeating_optimal(nums))