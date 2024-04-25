import timeit

def singelNumber(arr):
    dct = {}
    for n in arr:
        if n not in dct:
            dct[n] = 1
        else:
            dct[n] += 1

    for key in dct:
        if dct[key] == 1:
            return key

def singleNumber2(arr):
    result = 0
    for n in arr:
        result ^= n
    return result

arr = [7,1,2,1,2]

start_time = timeit.default_timer()
print(singelNumber(arr))
end_time = timeit.default_timer()
print(f"Time for singelNumber: {end_time - start_time}")

start_time = timeit.default_timer()
print(singleNumber2(arr))
end_time = timeit.default_timer()
print(f"Time for singleNumber: {end_time - start_time}")


#  פונקציות המרה לבינארי ודצימלי כעזר למעקב אחר הקוד ישנה הדפסה מעוצבת לחזות ויזואלית של הפעולה

def print_matrix(num1, num2):
    bin1 = format(num1, '04b')
    bin2 = format(num2, '04b')
    xor_result = num1 ^ num2
    bin_xor = format(xor_result, '04b')

    print(f"{bin1:<10}")
    print(f"{'----':<10}")
    print(f"{bin2:<10}")
    print(f"{'XOR in binary:':<15}{bin_xor:<10}")
    print(f"{'XOR in decimal:':<15}{xor_result:<10}")

print_matrix(1, 2)

