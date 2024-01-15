#  simple stack
# 1

def isValid(s):
    stuck = []
    dict = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in dict.values():
            stuck.append(char)
        elif len(stuck) == 0 or stuck.pop() != dict[char]:
            return False

    return not stuck


print(isValid(")("))



# more complex stack
# 2

def Valid_Parentheses(s):
    dictionary = \
        {"(": ")",
         "[": "]",
         "{": "}"
         }
    x = len(s)/2
    first = 0
    sec = 1
    list = [x for x in s]

    while len(list) > 0:
        if len(list) < 2:
            return False
        if list[0] in dictionary.values():
            return False
        if list[first] in dictionary and list[sec] == dictionary[list[first]]:
            list.pop(sec)
            list.pop(first)
            x -= 1
            first = 0
            sec = 1
        else:
            first += 1
            sec += 1

        if x == 0:
            return True
        if sec == len(list):
            return False
    return True



if __name__ == '__main__':

    print(isValid("(()())"))  # True
    print(isValid("(()()"))  # False

    print(Valid_Parentheses("(()())"))  # True
    print(Valid_Parentheses("(()()"))  # False

