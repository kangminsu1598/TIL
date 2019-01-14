
def countingsort(a, b, c):
    for i in range(len(a)):
        c[a[i]] += 1
    for i in range(1, len(c)):
        c[i] += c[i-1]
    for i in range(len(a)-1, -1, -1):
        b[c[a[i]]-1] = a[i] #B가 0부터 시작해서 -1 해준다
        c[a[i]] -= 1

a = [1,4,5,1,2,4,5,7,9,3,0,0]
b = [0]*len(a)
c = [0] * 10
countingsort(a, b, c)
print(b)