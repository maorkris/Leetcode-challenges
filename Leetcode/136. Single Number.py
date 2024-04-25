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

arr = [3,1,2,1,2] # Increase the size of the array to see a more noticeable difference in time

start_time = timeit.default_timer()
print(singelNumber(arr))
end_time = timeit.default_timer()
print(f"Time for singelNumber: {end_time - start_time}")

start_time = timeit.default_timer()
singleNumber2(arr)
end_time = timeit.default_timer()
print(f"Time for singleNumber: {end_time - start_time}")


print(3 ^10 )