import json

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    arr = json.loads(input().strip())


    def dfs(depth, nums):
        global ans

        depth += 1  # dfs호출될때마다 깊이를 1씩 증가해줍니다.

        for val in nums:
            if isinstance(val, int):  # 리스트에서 받아온 값이 무슨타입인지 확인합니다.
                ans += (val*depth)  # int형이면 해당 값을 깊이만큼 곱해서 ans에 더해줍니다.
            else:
                dfs(depth, val)  # int형이 아니면 문제상으로 리스트기 때문에 해당 리스트와 깊이를 dfs에 재귀로넘겨줍니다.


    ans = 0
    dfs(0, arr)  # 깊이 확인용 depth와 리스트를 같이 넘겨줍니다.
    print(f"#{tc} {ans}")