def find_pattern(text, pattern):
    M = len(pattern)  # 찾을 패턴의 길이
    N = len(text)  # 전체 텍스트의 길이

    i = 0  # 텍스트에서 검사를 시작할 위치
    j = 0  # 패턴의 비교 인덱스 위치

    # 문자열의 끝까지 가기 전에는 계속 비교를 한다.
    while i < N and j < M:
        if text[i] != pattern[j]:   # 각 인덱스 위치의 문자를 비교했더니, 패턴이 일치하지 않는다.
            i = i - j
            j = -1
        
        # i(원본 문자열의 비교 위치), j(패턴 문자열의 비교 위치)
        i += 1
        j += 1

    if j == M:
        return i - M
    else:
        return -1

# 예제 사용
str_main = "123456789"
str_sub = "456"

# 패턴의 시작 위치 찾기
result = find_pattern(str_main, str_sub)

if result != -1:
    print(f"패턴이 텍스트의 {result}번째 위치에서 발견되었습니다.")
else:
    print("패턴을 찾을 수 없습니다.")