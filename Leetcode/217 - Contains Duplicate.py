def Contains_Duplicate(nums):

    ndict = {}
    for i in nums:
        if i not in ndict:
            ndict[i] = 1
        else:
            ndict[i] += 1
            if ndict[i] == 2:
                return True
    else:
        return False

print(Contains_Duplicate([2,14,18,22,22])) # true
# solution 2:
def Contains_Duplicate2(nums):
    arr = sorted(nums)
    for i in range(len(arr) -1):
        if arr[i] in arr[i+1:]:
            return True
    else:
        return False

print(Contains_Duplicate2([2,14,18,22,22])) # true
