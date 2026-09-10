

# Input: nums = [10, 5, 2, 7, 1, 9],  k=15
#
# Output: 4
def longest_subarray_with_sum(nums, k):
    max_len = 0
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if sum(nums[i:j+1]) == k:
                max_len = max(max_len, j - i + 1)
    return max_len


def longest_subarray_with_sum_optimized(nums, k):
    prefix_sum = 0
    sum_indices = {0: -1}
    max_len = 0

    for i in range(len(nums)):
        prefix_sum += nums[i]

        if prefix_sum - k in sum_indices:
            max_len = max(max_len, i - sum_indices[prefix_sum - k])a

        if prefix_sum not in sum_indices:
            sum_indices[prefix_sum] = i

    return max_len

def longest_subarray_with_sum_two_pointer(nums, k):
    left = 0
    current_sum = 0
    max_len = 0

    for right in range(len(nums)):
        current_sum += nums[right]

        while current_sum > k and left <= right:
            current_sum -= nums[left]
            left += 1

        if current_sum == k:
            max_len = max(max_len, right - left + 1)

    return max_len

nums = [10, 5, 2, 7, 1, 9]
k=15

print(longest_subarray_with_sum(nums, k))
print(longest_subarray_with_sum_optimized(nums, k))
print(longest_subarray_with_sum_two_pointer(nums, k))