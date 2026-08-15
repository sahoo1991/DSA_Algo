# Input: nums1 = [1, 2, 2, 3, 5], nums2 = [1, 2, 7]
#
# Output: [1, 2]

def intersect(nums1, nums2):
    i,j = 0,0
    m, n = len(nums1), len(nums2)
    result = []
    while i < m and j < n:
        if nums1[i] < nums2[j]:
            i += 1
            continue
        elif nums1[i] == nums2[j]:
            result.append(nums1[i])
            i += 1
            j += 1
        else:
            j += 1
            continue
    return result


# nums1 = [1, 2, 2, 3, 5]
# nums2 = [1, 2, 7]
nums1 =  [1, 2, 2, 3, 3, 3]
nums2 =  [2, 3, 3, 4, 5, 7]
print(intersect(nums1, nums2))