# Input: nums1 = [1, 2, 3, 4, 5], nums2 = [1, 2, 7]
#
# Output: [1, 2, 3, 4, 5, 7]


def union_brute_force(nums1, nums2):
    m , n = len(nums1), len(nums2)
    i, j = 0, 0
    result = []
    while i < m and j < n:
        if nums1[i] < nums2[j]:
            if not result or nums1[i] != result[-1]:
                result.append(nums1[i])
            i += 1
        elif nums1[i] == nums2[j]:
            if not result or nums1[i] != result[-1]:
                result.append(nums2[j])
            j += 1
            i += 1
        else:
            if not result or nums2[j] != result[-1]:
                result.append(nums2[j])
            j += 1
    while i < m:
        if not result or result[-1] != nums1[i]:
            result.append(nums1[i])
        i += 1
    while j < n:
        if not result or result[-1] != nums2[j]:
            result.append(nums2[j])
        j += 1
    return result







# nums1 = [1, 2, 3, 4, 5]
# nums2 = [1, 2, 7]
nums1 =  [3, 4, 6, 7, 9, 9]
nums2 = [1, 5, 7, 8, 8]
print(union_brute_force(nums1, nums2))
