# 동시에 한 위치씩 검색 > 틀리면 원본은 다음 위치로, 패턴은 첫 위치로
# 반복 > 패턴 길이 만큼 순회되면 종료. 원본의 위치 출력

def bruteforce(text, pattern):
    idx = 0
    diff = 0
    for j in range(len(text)):
        for i in range(len(pattern)):
            if pattern[i] != text[j]:
                i = 0
                diff = 0
                idx += 1
                break
            else:
                j += 1
                diff += 1
        if len(pattern) == diff:
            return text[idx:(idx+len(pattern))]
    return -1

print(bruteforce('abcdefghj', 'ghi'))

