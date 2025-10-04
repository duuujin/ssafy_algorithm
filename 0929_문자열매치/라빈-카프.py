def rabin_karp_rolling_hash(text, pattern):
    n = len(text)   # 본문 문자열의 길이
    m = len(pattern)    # 패턴의 길이
    prime = 101    # 해시 값의 범위를 제한하기 위한(모듈러연산, m)
    base = 256   # 위치 값을 의미한다

    # 문자열을 해시값으로 바꾸는 함수
    def calculate_hash(str):
        hash_value = 0  # 해시값으로 바꾸는 과정에서 누적할 변수
        for i, char in enumerate(str):
            # ord: 아스키코드 값을 가져오는 내장함수 ord('a') -> 97을 뱉어요
            # pow: base(밑 값), m-1-i(지수)
            # 세번째 파라미터는 ? prime보다 커지지 않게 자체적으로 최적화하도록 하는것입니다
            hash_value += ord(char) * pow(base, m-1-i, prime)
        return hash_value % prime
    # 패턴의 해시값을 구한다.
    pattern_hash = calculate_hash(pattern)
    # 처음 시작 문자열의 해시값을 구한다.
    window_hash = calculate_hash(text[:m])

    # 최고 자릿수의 값을 미리 계산해놨다
    highest_power = pow(base, m-1, prime)


    for i in range(n - m + 1):
        if window_hash == pattern_hash:
            if text[i:i+m] == pattern:
                print(f"패턴: {i} - {i + m - 1}")

        if i < n - m:
            window_hash = window_hash - (ord(text[i]) * highest_power) % prime
            window_hash = (window_hash + ord(text[i + m])) % prime

# 테스트
text = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"
print(f"텍스트: {text}")
print(f"패턴: {pattern}")
rabin_karp_rolling_hash(text, pattern)
