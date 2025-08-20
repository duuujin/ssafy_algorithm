# 30분 이내 풀기 실패. 답 보고 재복습 하러 감
T = int(input())
for test_case in range(1,T+1):
    k, n, m = map(int,input().split()) # k = 한 번 충전 이동거리 n = 버스종점 길이 m = 충전기 갯수
    battery = list(map(int,input().split()))
    bus = [0]* (n+1)
    total_cnt = 0

    # for i in range(n+1):
    #     if i % k == 0:
    #         bus[i] += 1
    for ch in battery: # 충전기가 있는 위치 bus 리스트에 추가
        bus[ch] += 1
    
    print(bus)