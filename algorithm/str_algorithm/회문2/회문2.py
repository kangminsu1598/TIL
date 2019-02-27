import sys
sys.stdin = open("회문2_input.txt", "r")

a = range(100)

def p(s):
    for i in range(100, 0, -1): #회문의길이
        for k in range(0, 100 - i + 1): #앞에서 몇번째 글짜부터 시작해서 찾을지
            for g in s:
                if g[k] == g[k + i - 1]:
                    if g[k:k + i] == g[k:k + i][::-1]:
                        return i

for _ in range(10):
    t = input()
    s = [input() for _ in a]
    v = ["".join([s[v][h] for v in a]) for h in a]
    print(f"#{t} {max(p(s), p(v))}")
