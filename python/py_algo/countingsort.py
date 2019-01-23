
a = [1,4,5,1,2,4,5,7,9,3]
b = [0]*len(a)
c = [0] * 10

def countingsort(a, b, c):
    for i in range(len(a)):
        c[a[i]] += 1 # a 집합의 원소의 갯수를 c 집합에서 카운팅한다
    for i in range(1, len(c)):
        c[i] += c[i-1] # c[0]부터 c[n]까지 누적한다 > a의 각 원소 집합의 첫째 항 위치 설정
    for i in range(len(a)-1, -1, -1):
        b[c[a[i]]-1] = a[i] #결과 리스트 순서는 0부터 시작해서 -1 해준다,
        c[a[i]] -= 1 #a[i] 원소를 b집합에 추가하고, c 집합에서 차감한다


countingsort(a, b, c)
print(b)