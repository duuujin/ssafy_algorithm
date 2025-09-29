def boyer_moore_search(text, pattern):
    m = len(pattern)
    n = len(text)
    
    if m == 0 or n == 0 or m > n:
        return []

    # jump 할 거리를 저장할 사전이다
    skip_table = {}
    for i in range(m - 1):  # 마지막 문자(m-1)는 규칙에서 제외
        skip_table[pattern[i]] = m - 1 - i

    i = 0 
    found_indexes = []

    while i <= n - m:
        j = m - 1 

        while j >= 0 and pattern[j] == text[i + j]:
            j -= 1

        if j < 0:
            found_indexes.append(i)
            i += 1
        else:
            bad_char = text[i + j]
            
            shift = skip_table.get(bad_char, m)
            i += shift
            
    return found_indexes

text = "a pattern matching algorithm"
pattern = "rithm"
result = boyer_moore_search(text, pattern)

if result:
    print(f"패턴이 발견된 위치: {result}")
else:
    print("패턴을 찾지 못했습니다")
