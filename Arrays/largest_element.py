def largest_element(array):
    if len(array) == 0:
        raise ValueError("array is empty")
    largest = array[0]
    for element in array:
        if element > largest:
            largest = element
    return largest


nums = [3, 3, 0, 99, -40]
print(largest_element(nums))