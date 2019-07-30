# Given a list of integers, find the index of the two numbers that adds up to target
# suppose all the integers are distinct and there is only one solution
# ex. [7, 1, 5, 2, 0, 4] with target 8 would return [0, 1] else return false


def two_sum(nums, target):
    existing_nums = {}
    for ind, num in enumerate(nums):
        if num in existing_nums:
            return [existing_nums[num], ind]
        existing_nums[target - num] = ind

    return False


print(two_sum([7, 1, 5, 2, 0, 4], 8))
