def boyer_moore(text, pattern):
    # 원본의 인덱스 i, 패턴의 요소 j
    for i in range(len(pattern),len(text)+1):
        print(text[i])
    
        pattern_count = 1
        # 스트링을 뒤에서 부터 뽑아야함...
        for j in pattern[::-1]:
            if j == pattern[-1] and text[i] == j:
                i += len(pattern)
            if j != pattern[-1] and text[i] == j:
                i += pattern_count
            
    return 0 

text = 'abcscaseqwerfxzvasdlepdacasdefasdef'
pattern = 'def'

boyer_moore(text, pattern)