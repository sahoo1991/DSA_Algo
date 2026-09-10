

# Input: nums = [1, 2, 3], k = 3
#
# Output: 2
def count_longest_subarray_with_sum(nums, k):
    count = 0
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if sum(nums[i:j+1]) == k:
                count +=1
    return count


def count_subarrays_with_sum_optimized(nums, k):
    prefix_sum = 0
    sum_indices = {0: 1}
    count = 0

    for i in range(len(nums)):
        prefix_sum += nums[i]
        diff = prefix_sum - k
        count += sum_indices.get(diff, 0)

        sum_indices[prefix_sum] = sum_indices.get(prefix_sum, 0) + 1

    return count


# nums = [1, 2, 3]
# k = 3
nums = [-5,-3,0,-9,-6,1,5,-7,-1,0,3,5,9]
k = 0


print(count_longest_subarray_with_sum(nums, k))
print(count_subarrays_with_sum_optimized(nums, k))