def monster(lst):
    left = []
    right = []
    length = len(lst)

    left_s = 0
    left_e = 0

    for i in range(length - 1):
        left_e += 1
        print(lst[left_e - 1])
        print(lst[left_e])
        if lst[left_e - 1] <= lst[left_e]:
            left.append(lst[left_s:left_e])
            left_s = left_e

    return left


print(monster([1, 2, 3, 4, 8, 7, 6, 5]))
