# פיתרון 1
def move_zeros (nums):
    for j in nums:
        flag = False
        for i in range(len(nums) - 1):
                if nums[i] == 0 and nums[i + 1] != 0:
                    nums[i],nums[i + 1] = nums[i + 1], nums[i]
                    flag = True
        if not flag:
            return nums
    return nums


# פיתרון 2
def move_zeros(nums):
    non_zero_idx = 0  # אינדקס לאיתור הערך שאינו 0 הבא

    # עובר על כל איבר במערך
    for i in range(len(nums)):
        # אם האיבר שונה מאפס
        if nums[i] != 0:
            # מחליף את האיבר עם האיבר בעמדת non_zero_idx
            nums[i], nums[non_zero_idx] = nums[non_zero_idx], nums[i]
            # מעדכן את non_zero_idx
            non_zero_idx += 1

    return nums

