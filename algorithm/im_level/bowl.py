data = input()
value = 10
for i in range(1,len(data)):
    if data[i] != data[i-1]:
        value += 10
    else:
        value += 5
print(value)