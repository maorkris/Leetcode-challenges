# Difficulty: Easy
# 28. Find the Index of the First Occurrence in a String
# Given two strings haystack and needle, return the index of the first occurrence of needle in haystack,
# or -1 if needle is not part of haystack.

#  example 1:
# Input: haystack = "hello", needle = "ll"
# Output: 2

#  example 2:
# Input: haystack = "aaaaa", needle = "bba"
# Output: -1

#  example 3:
# input: haystack = "rmkler", needle = "kler"
# output: 2


#  solution1:


def strStr(haystack: str, needle: str) -> int:

    if needle not in haystack:
        return -1
    con = 0
    while con < len(haystack):
        if needle in haystack[con : con + len(needle)]:
            return con
        else:
            con += 1


print(strStr("hello", "ll"))