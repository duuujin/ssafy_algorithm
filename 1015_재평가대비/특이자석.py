from collections import deque

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    mags = [deque(map(int, input().split())) for _ in range(4)]

    for _ in range(n):
        idx, d = map(int, input().split())
        idx -= 1  # index로 변환

        will = [0, 0, 0, 0]
        will[idx] = d
        # 오른쪽
        for i in range(idx, 3):
            if mags[i][2] != mags[i+1][6]:
                will[i+1] = -will[i]
            else:
                break
        # 왼쪽
        for i in range(idx, 0, -1):
            if mags[i][6] != mags[i-1][2]:
                will[i-1] = -will[i]
            else:
                break
        # 회전
        for i in range(4):
            if will[i] == 1:   mags[i].rotate(1)
            elif will[i] == -1:mags[i].rotate(-1)
    # 점수 계산
    ans = 0
    for i in range(4):
        if mags[i][0] == 1:
            ans += 2**i

    print(f'#{tc} {ans}')