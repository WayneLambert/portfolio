# FizzBuzz implementation with reversal of string

for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print('zzuBzziF'[::-1])
    elif num % 3 == 0:
        print('zziF'[::-1])
    elif num % 5 == 0:
        print('zzuB'[::-1])
    else:
        print(num)
