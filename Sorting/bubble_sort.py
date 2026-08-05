def bubble_sort(ls):
    # flag can be added to optimize this.
    if len(ls) <= 1:
        return
    for i in range(len(ls) - 1):
        for j in range(len(ls) -1):
            if ls[j] > ls[j+1]:
                 ls[j], ls[j+1] = ls[j+1], ls[j]


ls = [10, 5, 3, 25, 19, 11]
bubble_sort(ls)
print(ls)

# TC - O(n2)
# SC - O(1)
