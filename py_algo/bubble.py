l = [55, 7, 78, 12, 42, 3]

def bubble(a):
    for i in range(len(l)-1, 0, -1):
        for j in range(i):
            if l[j] < l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]

    print(l)

bubble(l)

