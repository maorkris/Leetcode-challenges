def Top_K_Frequent_Elements(nums):

    dict = {}
    for i in nums:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1

    bigger = None
    second = None
    for key in dict:
        if bigger == None or dict[key] > dict[bigger]:
            second = bigger
            bigger = key
        elif second == None or dict[key] > dict[second]:
            second = key

        elif bigger and second:
            if bigger > second:
                return [bigger, second]
            else:
                return [second, bigger]

    else:
        return [bigger]

print(Top_K_Frequent_Elements([4,1,-1,2,-1,2,3])) # [2,-1]

