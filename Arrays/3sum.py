

# Input: nums = [2, -2, 0, 3, -3, 5]
#
# Output: [[-2, 0, 2], [-3, -2, 5], [-3, 0, 3]]

def get_triplets_brute(ls):
    result = []
    for i in range(len(ls) - 2):
        for j in range(i+1, len(ls) - 1):
            for k in range(j+1, len(ls)):
                if ls[i] + ls[j] + ls[k] == 0:
                    result.append(sorted([ls[i], ls[j], ls[k]]))
    return result

def get_triplet_better(ls):
    result = set()
    temp = {}
    for i in range(len(ls)):
        for j in range(i+1, len(ls)):
            num = -(ls[i] + ls[j])
            if num in temp:
                result.add(tuple(sorted([num, ls[i], ls[j]])))
            else:
                temp[ls[j]] = 1
    return result


def get_triplet_optimal(ls):
    ls.sort()
    result = []
    for i in range(len(ls)):
        if i > 0 and ls[i] == ls[i-1]:
            continue
        j = i + 1
        k = len(ls) - 1
        while j < k:
            if ls[i]  + ls[j] + ls[k] == 0:
                result.append(sorted([ls[i], ls[j], ls[k]]))
                j += 1
                k -= 1
                while ls[j] == ls[j-1] and j < k:
                    j += 1
                while ls[k] == ls[k + 1] and k> j:
                    k -= 1
            elif ls[i]  + ls[j] + ls[k] < 0:
                j += 1
            else:
                k -= 1
    return result




nums = [2, -2, 0, 3, -3, 5]
print(get_triplet_optimal(nums))