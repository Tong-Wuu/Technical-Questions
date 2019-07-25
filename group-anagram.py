# given a list of strings, group all the anagram in
# the form of listof listof strings
# ex. given [eat, tea, tan, nat, bat, ate] return
#   -> [[eat, tea, ate], [tan, nat], [bat]]

# solution 1

# One way to determine wether two strings are anagrams is by
# sorting both strings. If both sorted string is the same therefore
# the strings are anagrams

# 1) for each string, sort it, make it a key
# 2) with the sorted key, append the cur string
# 3) by using the get() function, it sets default value to a list
# 4) therefore we can try to get the already sorted key value and append the cur string
# 5) or the key doesn't exist we can append the cur string to it


def groupAnagram_sol_1(strs):
    res = {}
    for ele in strs:
        key = ''.join(sorted(list(ele)))
        res[key] = res.get(key, [])
        res[key].append(ele)

    return res.values()

# solution 2

# Another way to approach this is by using the defaultdict function
# from the collections library

# the defaultdict function provides the functionality of dictionaries
# but have default values if the key hasn't been set yet


def groupAnagram_sol_2(strs):
    from collections import defaultdict
    res = defaultdict(list)
    for ele in strs:
        res[''.join(sorted(ele))].append(ele)

    return res.values()
