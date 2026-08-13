def get_max_consecutive_one(value):
    count = 0
    max_count = 0
    for num in value:
        if num == 1:
            count += 1
        else:
            if count > max_count:
                max_count = count
            count = 0
    if count > max_count:
        max_count = count
    return max_count

nums = [1, 1, 0, 0, 1, 1, 1, 0, 1,1,1,1,1]
print(get_max_consecutive_one(nums))
