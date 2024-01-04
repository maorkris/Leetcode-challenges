

def longestCommonPrefix2(strs):
    res = ""
    for i in range(len(strs[0])):
        for s in strs:
            if i == len(s) or s[i] != strs[0][i]:
                return res
        else:
            res += strs[0][i]
    return res


def longestCommonPrefix(strs):
    if len(strs) == 0:
        return ""
    if len(strs) == 1:
        return strs[0]
    strs.sort()
    res = ""
    for i in range(len(strs[0])):
        if strs[0][i] == strs[-1][i]:
            res += strs[0][i]
        else:
            break
    return res
if __name__ == "__main__":

    print(longestCommonPrefix2(["flower","flow","flight"]))
    pass
