# I = 1, V = 5, X = 10, L = 50, C = 100, D = 500, M = 1000

def romanToInt(roman_num):
    roman_table = \
        {"I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000}

    # משתנה שמחזיק את התוצאה
    result = 0

    # לולאה שעוברת על כל התווים במספר הרומי
    for i in range(len(roman_num)):
        # בדיקה אם אנחנו לא בתו האחרון של המחרוזת
        if i < len(roman_num) - 1:
            # בדיקה אם הערך של התו הנוכחי קטן מהערך של התו הבא
            if roman_table[roman_num[i]] < roman_table[roman_num[i + 1]]:
                # אם כן, מחסירים את הערך של התו הנוכחי מהתוצאה
                result -= roman_table[roman_num[i]]
            else:
                # אם לא, מוסיפים את הערך של התו הנוכחי לתוצאה
                result += roman_table[roman_num[i]]
        else:
            # אם אנחנו בתו האחרון של המחרוזת, מוסיפים את הערך של התו הנוכחי לתוצאה
            result += roman_table[roman_num[i]]

    # הדפסת התוצאה
    print(result)
romanToInt("MCMXCIV")