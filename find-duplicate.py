# Given a list of integers, find if there is duplicate in the list


def duplicate(nums):
    return len(set(nums)) != len(nums)


def duplicate2(nums):
    from collections import Counter
    if len(nums) <= 1:
        return False

    num = Counter(nums)
    return max(num.values()) > 1


print(duplicate([1, 2, 3, 4, 4, 5]))
print(duplicate2([1, 2, 3, 4, 4, 5]))
