# Input: nums = [1, 0, 2, 1, 0]
#
# Output: [0, 0, 1, 1, 2]

def sort_0s_brute(ls):
    zeroes = []
    ones = []
    twos = []
    result = []
    for num in ls:
        if num == 0:
            zeroes.append(0)
        elif num == 1:
            ones.append(1)
        else:
            twos.append(2)
    result.extend(zeroes)
    result.extend(ones)
    result.extend(twos)
    return result

def sort_0s_better(ls):
    index_i = -1
    for temp in range(len(ls)):
        if ls[temp] != 0:
            index_i = temp
            break
    for j in range(index_i + 1, len(ls)):
        if ls[j] == 0:
            ls[index_i], ls[j] = ls[j], ls[index_i]
            index_i += 1
    for j in range( index_i, len(ls)):
        if ls[j] == 1:
            ls[index_i], ls[j] = ls[j], ls[index_i]
            index_i += 1
    for j in range( index_i, len(ls)):
        if ls[j] == 2:
            ls[index_i], ls[j] = ls[j], ls[index_i]
            index_i += 1

def sort_0s_optimal(ls):
    # Dutch National Flag algorithm
    low, mid, high = 0, 0, len(ls) -1
    while mid <= high:
        if ls[mid] == 0:
            ls[low], ls[mid] = ls[mid], ls[low]
            low += 1
            mid += 1
        elif ls[mid] == 1:
            mid += 1
        else:
            ls[mid], ls[high] = ls[high], ls[mid]
            high -= 1







nums = [1, 0, 2, 1, 0]
print(sort_0s_optimal(nums))
print(nums)

