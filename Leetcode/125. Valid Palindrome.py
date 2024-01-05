def isPalindrome(s):
    from_start = 0
    from_end = len(s) - 1
    while from_start < from_end:
        while not s[from_start].isalnum() and from_start < from_end:
            from_start += 1
        while not s[from_end].isalnum() and from_start < from_end:
            from_end -= 1
        if from_start < from_end and s[from_start].upper() != s[from_end].upper():
            return False
        from_start += 1
        from_end -= 1
    return True


print(isPalindrome("A MAN, a plan, a canal: Panama")) #--> True
print(isPalindrome("race a car")) # --> False
print(isPalindrome("0P")) #--> False
print(isPalindrome("ab_a"))  #--> True
