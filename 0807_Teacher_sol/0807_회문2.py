# 회문을 검사하는 재귀함수
# word : 검사해야하는 문자열
# left : 왼쪽에서 다가오는 포인터
# right : 오른쪽에서 다가오는 포인터
def is_palindrome(word,left,right):
    # 종료조건
    # left와 right가 교차하지 않으면, 서로 검사를 해야한다.
    # left와 right가 교차했다는건 ==> 서로 비교검사를 통과
    if left >= right:
        return True
    
    # 주어진 두 포인터로 비교했을 때, 다르면 바로 False
    if word[left] != word[right]:
        return False

    return is_palindrome(word,left + 1, right - 1)

T = int(input())
for test_case in range(1, T+1):
    # strip은 양쪽 공백 제거
    # 이거 swea 문제 풀때, 간혹 내 코드는 문제 x
    # 공백 때문에 안돌아 갈 경우 분명 있음.
    word = input().strip()
    n = len(word)
    # 재귀함수
    # 범위가 점점 줄어야하고, 종료조건이 있어야함
    
    reuslt = is_palindrome()
        
    print(f'#{test_case}')