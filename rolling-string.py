# Given a string and list of numbers, roll the string by the character with the roll
# indicating the substring to roll
# roll -> increment by 1
# For example: given string = "abc", given list of integer = [3,2]
# roll once where the substring is the range of "abc", then
# roll once where the substring is the range of "ab"


def solution_1_roll(s, roll):
    result = ""
    sumOfEachRoll = [0] * len(s)
    a_to_z = [chr(i) for i in range(97, 123)]

    for eachRoll in roll:
        for i in range(eachRoll):
            sumOfEachRoll[i] += 1

    for char in range(len(s)):
        index = (ord(s[char]) + sumOfEachRoll[char] - 97) % 26
        result += a_to_z[index]

    return result


def solution_2_roll(s, roll):
    ordChar = [ord(char) for char in s]

    for eachRoll in roll:
        for char in range(0, eachRoll):
            if ordChar[char] == 122:
                ordChar[char] = 97
            else:
                ordChar[char] += 1

    return ''.join(chr(char) for char in ordChar)


def solution_3_roll(s, roll):
    # 1) map each character to ord
    # 2) for each roll, add one to substring range
    # 3) map again to check the index
    # 4) map integers back to chr with index

    def get_sum_each_roll(roll):
        initSumOfEachRoll = [0] * len(s)
        for ind in range(0, roll):
            initSumOfEachRoll[ind] += 1
        return initSumOfEachRoll

    def do_sum_lists(lst_1, lst_2):
        return [sum(x) for x in zip(lst_1, lst_2)]

    def check_position(num):
        a_to_z = [chr(i) for i in range(97, 123)]
        return a_to_z[(num - 97) % 26]

    listOfChar = map(lambda x: x, s)  # convert string into list of char
    ordChar = map(lambda x: ord(x), listOfChar)  # convert each char to ord int
    eachRoll = map(get_sum_each_roll, roll)  # for each roll find the substring chars
    from functools import reduce
    sumOfEachRoll = reduce(do_sum_lists, eachRoll)  # reduce to find the sum
    rolled = [sum(x) for x in zip(ordChar, sumOfEachRoll)]  # sum total rolled number for each char
    check = map(check_position, rolled)  # check and turn back the char

    return ''.join(check)  # join the characters


def solution_4_roll(s, roll):
    import collections
    counter = collections.Counter(roll)
    sumCounter = sum(counter.values())
    ordChar = [ord(char) for char in s]

    for i in range(len(ordChar)):
        cur_roll = sumCounter - counter.get(i, 0)
        ordChar[i] += cur_roll

    return ''.join(chr(char) for char in ordChar)


print(solution_4_roll("abc", [3, 3, 2, 3, 3, 3]))
print(solution_2_roll("abc", [3, 3, 2, 3, 3, 3]))
