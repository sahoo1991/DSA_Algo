def insertion_sort(ls):
    if len(ls) <= 1:
        return
    for i in range(len(ls)):
        key = ls[i]
        j = i-1
        while ls[j] > key and j>=0:
            ls[j+1] = ls[j]
            j -= 1
        ls[j+1] = key



ls = [10, 5, 3, 25, 19, 11]
insertion_sort(ls)
print(ls)

# TC - O(n2)
# SC - O(1)
