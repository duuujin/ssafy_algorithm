T = int(input())
for test_case in range(1,T+1):
    s = input()
    
    def mirror_str(s):
        mirror_dict = { # 입력받을 문자열은 'b','d','p','q' 고정
        'b' : 'd',          # 딕셔너리 형태로, 키와 벨류 지정
        'd' : 'b',          # b,d  - d,b 는 , 순방향으로 찾을수도있지만,
        'p' : 'q',          # d로 들어오면 복잡해져서 역방향도 생각
        'q' : 'p'
        }
        mirrored = ""       # 빈문자열 만들어둔 뒤
        for ch in s:    # 반복문으로 하나씩 순회하면서 빈문자열에 추가
            mirrored += mirror_dict[ch]
        return mirrored[::-1]   # 마지막으로 뒤에서부터 읽도록 반환
    
    result = mirror_str(s)  # result 값에 할당 후 출력 
    print(f'#{test_case} {result}')