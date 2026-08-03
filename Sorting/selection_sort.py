def selection_sort(ls):
    if len(ls) <= 1:
        return
    for i in range(len(ls)):
        min_ind = i
        for j in range(i + 1, len(ls)):
            if ls[j] < ls[min_ind]:
                min_ind = j
        ls[i], ls[min_ind] = ls[min_ind], ls[i]


ls = [10, 5, 3, 25, 19, 11]
selection_sort(ls)
print(ls)

# TC - O(n2)
# SC - O(1)
