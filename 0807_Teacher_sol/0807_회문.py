T = int(input())
for test_case in range(1, T+1):
    # strip은 양쪽 공백 제거
    # 이거 swea 문제 풀때, 간혹 내 코드는 문제 x
    # 공백 때문에 안돌아 갈 경우 분명 있음.
    word = input().strip()

    # 회문 검사 후에 문제가 없다면 1을 반환.
    # 문제가 있다면 0으로 바꾸고 출력
    result = 1

    # 회문을 검사하는 로직을 작성하자.
    # 회문 -> 앞 뒤가 똑같은 문자열
    # 양쪽 끝에 인덱스를 놓고, 범위를 점점 좁혀가면서 비교를 할거다.
    # 문자열 길이의 절반까지 진행

    n = len(word) # 주어진 문자열의 길이
    # 시작점과 끝점에서 서로 다가오기 때문 절반까지만 인덱스를 진행
    for idx in range(n // 2):
        # 시작점의 인덱스와 끝점의 인덱스가 서로 다르면 false
        # 달라버리면 안쪽은 더이상 검사를 할 필요가 없으니 break
        if word[idx] != word[n - 1 - idx]:
            result = 0
            break
        
    print(f'#{test_case} {result}')