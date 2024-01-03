#121 -> True
#123 -> False
# "abc" -> False
# "civic" -> True

# solution1:
def palindrome(num):
    return str(num) == str(num)[::-1]


# print(palindrome("civic"))

# solution2:
def palindrome2(num):
    num = str(num)
    for i in range(len(num)):
        if num[i] != num[len(num) - 1 - i]:
            return False
    return True


# solution3:
def palindrome3(num):
    tmp = num
    rev = 0
    while num > 0:
        dig = num % 10
        rev = (rev * 10) + dig
        num = num // 10
    return tmp == rev


# solution 5 - 13/12/23
def pilah(s):
    right = 0
    left = len(s) - 1
    for i in range(len(s) // 2):
        if s[right] != s[left]:
            return False
        else:
            return True


if __name__ == '__main__':
    # print(palindrome("civic"))
    # print(palindrome2("ABA"))
    # print(palindrome3(45654))
    # print(pilah("aba"))
    pass
