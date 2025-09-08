T = int(input())
for test_case in range(1,T+1):
    n,k1,k2 = map(int,input().split())
    nums = [i for i in range(1,n+1)]
    ans = 0

    k = 2**n
    for i in range(k):
        sum_num = 0
        for j in range(n):
            if (i >> j) & 1:
                sum_num += nums[j]
            if sum_num > k2 :
                break
        if k1 <= sum_num <= k2:
            ans += 1
    print(ans)