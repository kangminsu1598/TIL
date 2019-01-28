def itoa(x):
    str = list()
    remainder = 0
    while True:
        remainder = x % 10
        str.append(chr(48+remainder))
        x //= 10
        if x == 0:
            break
    str = ''.join(reversed(str))
    return str
print(itoa(493))
