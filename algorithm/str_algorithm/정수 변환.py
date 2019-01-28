def atoi(string):
    value = 0
    count = 0
    while (count < len(string)):
        c = string[count]
        if c >= '0' and c <= '9':
            digit = ord(c) - ord('0')
        else:
            break
        value = (value * 10) + digit;
        count += 1
    return value

print(atoi('2'))


