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


print(solution_1_roll("abc", [3, 3, 3, 3, 3, 2]))
print(solution_2_roll("abc", [3, 3, 3, 3, 3, 2]))
