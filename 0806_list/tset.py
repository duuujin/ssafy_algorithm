T = 1

for test_case in range(1, T + 1):
    tc = int(input())
    num_len = 3
    result = []

    for i in range(num_len):
        num_list = list(map(int,input().split()))
        result.append(num_list)

        print(result)