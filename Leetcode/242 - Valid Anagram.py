# Difficulty: Easy
# source: https://leetcode.com/problems/valid-anagram/
# 242. Valid Anagram
# solution 1


""" Given two strings s and t , write a function to determine if t is an anagram of s.
    Example 1:
    Input: s = "anagram", t = "nagaram"
    Output: true

    Example 2:
    Input: s = "rat", t = "car"
    Output: false
    """

def Valid_Anagram (s, t):
    s = sorted(s)
    t = sorted(t)
    return s == t

# solution 2
def Valid_Anagram2(s,t):
    sdict = {}
    tdict = {}
    for i in s:
        if i not in sdict:
            sdict[i] = 1
        else:
            sdict[i] += 1

    for j in t:
        if j not in tdict:
            tdict[j] = 1
        else:
            tdict[j] += 1

    return sdict == tdict




if __name__ == '__main__':
    print(Valid_Anagram("anagram", "nagaram")) # True
    print(Valid_Anagram("rat", "car")) # False
    print(Valid_Anagram("a", "ab")) # False

    print(Valid_Anagram2("anagram", "nagaram")) # True
    print(Valid_Anagram2("rat", "car")) # False
    print(Valid_Anagram2("a", "ab")) # False
    pass
