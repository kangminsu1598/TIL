def bit_print(a):
    for i in range(7,-1,-1):
        if a & (1<<i):
            print(1, end='')
        else:
            print(0, end='')

a = 0x86
key = 0xAA
# print("a       ==>", end= "")
bit_print(a)