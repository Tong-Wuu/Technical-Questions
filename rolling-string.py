# Given a string and list of numbers, roll the string by the character with the roll
# indicating the substring to roll
# roll -> increment by 1
# For example: given string = "abc", given list of integer = [3,2]
# roll once where the substring is the range of "abc", then
# roll once where the substring is the range of "ab"


def roll(s, roll):
    result = ""
    sumOfEachRoll = [0] * len(s)
    a_to_z = [chr(i) for i in range(97, 123)]

    for eachRoll in roll:
        for i in range(len(sumOfEachRoll)):
            sumOfEachRoll[i] += 1

    for char in range(len(s)):
        index = (ord(s[char]) + sumOfEachRoll[char] - 97) % 26
        result += a_to_z[index]

    return result


print(roll("abc", [3]))
