#  you need to calculate the length of last word in a string.


def lengthOfLastWord(s):
    length = 0
    for i in range(len(s)):
        from_end = s[-i - 1]
        if from_end.isalpha():
            length += 1
        elif length == 0:
            continue
        else:
            return length
    else:
        return length

print(lengthOfLastWord("Hello World")) # 5
print(lengthOfLastWord("a ")) # 1
print(lengthOfLastWord(" ")) # 0
print(lengthOfLastWord("   fly me   to   the moon  ")) # 4