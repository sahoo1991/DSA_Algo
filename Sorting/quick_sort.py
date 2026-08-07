def quick_sort_pythonic_way(ls):
    # This is pythonic way to sort but its not in-place. Keep this in mind
    if len(ls) <= 1:
        return ls
    pivot = ls[-1]
    left_arr = [el for el in ls if el < pivot]
    right_arr = [el for el in ls if el > pivot]
    return quick_sort_pythonic_way(left_arr) + [pivot] + quick_sort_pythonic_way(right_arr)


def get_pivot_index_lomuto(ls, low, high):
    # using Lomuto Partition Scheme
    pivot = ls[high]
    i = low - 1
    for j in range(low, high):
        if ls[j] <= pivot:
            i += 1
            ls[i], ls[j] = ls[j], ls[i]
    ls[i + 1], ls[high] = ls[high], ls[i + 1]
    return i + 1


def get_pivot_index_raw(ls, low, high):
    pivot = ls[high]
    i, j = low, high
    while i < j:
        while ls[i] <= pivot and i <= high - 1:
            i += 1
        while ls[j] >= pivot and j >= low + 1:
            j -= 1
        if i < j:
            ls[i], ls[j] = ls[j], ls[i]
    ls[low], ls[j] = ls[j], ls[low]
    return j


def quick_sort_in_place(ls, low, high):
    if low < high:
        pivot_index = get_pivot_index_raw(ls, low, high)
        quick_sort_in_place(ls, low, pivot_index - 1)
        quick_sort_in_place(ls, pivot_index + 1, high)


ls = [10, 5, 3, 25, 19, 11]
print(quick_sort_pythonic_way(ls))
print(ls)  # original list remains unchanged
print(quick_sort_in_place(ls, 0, len(ls) - 1))
print(ls)  # original list changed

# TC - O(n2) - Pythonic way
# SC - O(n log n)
