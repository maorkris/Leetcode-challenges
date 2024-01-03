# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

#           solution 1
def twoSum(nums,target):
    for index1 in range(len(nums)):
        for index2 in range( index1 + 1,len(nums)):
            if nums[index1] + nums[index2] == target:
                array = (index1,index2)
                return array

#          solution 2 - 58 ms

def twoSum2(nums,target):
    seen = {}
    for i in range(len(nums)):
        if target - nums[i] in seen:
            return seen[target - nums[i]] , i
        else:
            seen[nums[i]] = i

#          solution 3

def twoSum3(nums,target):
    dict = {}
    for index , value in enumerate( nums):
        result = target - value
        if result in dict:
            return [dict[result], index]
        else:
            dict[value] = index


# 14
# 14
def add_numbers(num,arr):
    arr1 = []
    con = 0
    for i in range(0,len(arr)):
        for j in range(0,len(arr)):
            if arr[i] + arr[j] == num:
                con = j , i
        arr1.append(con)
    return arr1


#        solution 4 13.12.23

def two_sum(nums,target):
    for i in range(len(nums)):
        for j in range(i + 1,len(nums)):
            if nums[i] + nums[j] == target:
                return (i,j)


if __name__ == '__main__':

    # print(twoSum([3,4,6,1],5))
    # print(twoSum2([3,4,6,1],5))
    # print(twoSum3([3,4,6,1],5))
    # print(add_numbers(9, [2,7,11,15]))
    # print(two_sum([2,5,5,11],10))
    pass