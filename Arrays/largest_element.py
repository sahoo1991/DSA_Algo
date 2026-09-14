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
# Time Complexity: O(n) - The function iterates through the array once, where n is the number of elements in the array.
# Space Complexity: O(1) - The function uses a constant amount of space regardless of the input size.