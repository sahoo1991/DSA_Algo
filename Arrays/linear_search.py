# find the number and return the index of the number, return -1 if not found

def linear_search(array, value):
    for index, item in enumerate(array):
        if item == value:
            return index
    return -1



ls = [7, 4, 1, 5, 3]
print(linear_search(ls, 10))