#
# Input : nums = [4, 2, 2, 6, 4], k = 6
#
#
#
# Output : 4
#
#
#
# Explanation : The subarrays having XOR of their elements as 6 are [4, 2],  [4, 2, 2, 6, 4], [2, 2, 6], and [6]


def count_subarrays_with_given_xor_brute(nums, k):
    count = 0
    n = len(nums)

    for i in range(n):
        current_xor = 0
        for j in range(i, n):
            current_xor ^= nums[j]
            if current_xor == k:
                count += 1

    return countm m

def count_subarrays_with_given_xor_optimized(nums, k):
    count = 0
    prefix_xor = 0
    xor_map = {}

    for num in nums:
        prefix_xor ^= num

        if prefix_xor == k:
            count += 1

        required_xor = prefix_xor ^ k
        count += xor_map.get(required_xor, 0)

        xor_map[prefix_xor] = xor_map.get(prefix_xor, 0) + 1

    return count






nums = [4, 2, 2, 6, 4]
k = 6
print(count_subarrays_with_given_xor_brute(nums, k))
print(count_subarrays_with_given_xor_optimized(nums, k))