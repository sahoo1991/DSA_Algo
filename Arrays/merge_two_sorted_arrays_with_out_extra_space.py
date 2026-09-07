
def merge(nums1, m, nums2, n):
    # Start from the end of both arrays
    i, j, k = m - 1, n - 1, m + n - 1

    while j >= 0:
        if i >= 0 and nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1









nums1 = [-5, -2, 4, 5, 0, 0, 0]
nums2 = [-3, 1, 8]
merge(nums1, 4, nums2, 3)
print(nums1)