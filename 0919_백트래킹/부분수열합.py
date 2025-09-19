# T = int(input())
# for test_case in range(1,T+1):
#     n, m = map(int,input().split())
#     nums = list(map(int,input().split()))

#     k = 2 ** n
#     ans = 0
#     for i in range(k):
#         sum_num = 0
#         for j in range(n):
#             if (i >> j) & 1 :
#                 sum_num += nums[j]
#         if sum_num == m: 
#             ans += 1
#     print(f'#{test_case} {ans}')

    # -----------------------------------------

T = int(input())
for test_case in range(1,T+1):
    def solution(idx, num_sum, cnt):
        global ans
        if num_sum == k:
            ans += 1
            return  
        if num_sum >= k : return
        if idx == len(nums): return

        solution(idx+1,num_sum+nums[idx],cnt+1)

        solution(idx+1,num_sum , cnt)
    
    n , k = map(int,input().split())
    nums = list(map(int,input().split()))
    ans = 0

    solution(0,0,0)
    print(f'#{test_case} {ans}')