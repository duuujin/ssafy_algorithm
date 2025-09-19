def find_subsets(idx,num_sum, num_sum_list):
    global result
    # 중간에 누적합이 목표 값과 동일해지면, 해당 선택 목록을 결과에 추가하고 끝냄
    if num_sum == target_sum:
        result.appned(num_sum_list)
        return

    # 누적합이 이미 target_sum을 넘어선 순간, 뒤에 경우의 수는 자르기. 
    # ( 가지치기 )
    if num_sum >= target_sum: return

    if idx == len(nums): return

    # idx에 해당하는 숫자를 고르거나
    find_subsets(idx+1, num_sum+nums[idx], num_sum_list + nums[idx])

    # idx에 해당하는 숫자를 고르지 않거나
    find_subsets(idx+1, num_sum, num_sum_list)

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target_sum = 10
result = []

# 문제에서 원하는건 , 10에 도달하는것
# 10이 되기 위한 값들 목록을 결과에 출력
# dfs 작성 시 필요한 것은
# 1. 종료조건 -> idx(선택 할지 말지 결정할 숫자인덱스)
# 2. 누적해서 가져가고 싶은 값(내가 선택한 숫자 리스트)
# 누적해서 더한 값도 그냥 같이 보내기
find_subsets(0, 0, [])