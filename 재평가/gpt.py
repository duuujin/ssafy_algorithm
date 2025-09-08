# num = [1,2,3,7]
# target = 6

# k = 2**len(num)
# for i in range(k):
#     sum_num = 0
#     for j in range(len(num)):
#         if (i >> j) & 1 == 1:
#             sum_num += num[j]
#     if sum_num == target:
#         print(True)
#         break
# else:
#     print(False)

# nums = [3,34,4,12,5,2]
# target = 10
# max_sum = 0
# k = 2** len(nums)
# for i in range(k):
#     sum_num = 0
#     for j in range(len(nums)):
#         if (i>>j) & 1:
#             sum_num += nums[j]
#     if sum_num <= target:
#         max_sum=max(max_sum,sum_num)
# print(max_sum)

T = int(input())
for test_case in range(1,T+1):
    n,k = map(int,input().split())
    nums = [1,2,3,4,5,6,7,8,9,10,11,12]
    count = 0

    s = 2**len(nums)
    for i in range(s):
        subset_sum = 0
        subset_count = 0
        for j in range(len(nums)):
            if (i >> j) & 1:
                subset_sum += nums[j]
                subset_count += 1
        if subset_count == n and subset_sum == k:
            count += 1
    print(count)