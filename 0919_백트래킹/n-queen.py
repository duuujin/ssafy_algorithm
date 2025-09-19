import pprint
# 현재 위치에 퀸을 놓을 수 잇는 검사하는 함수
# row: 행(가로) , col: 열(세로)
def is_valid_pos(board, row, col):
    # 현재 열에 다른 퀸이 있는지를 검사
    for i in range(row):
        if board[i][col] == 1:
            return False
        
    # 대각선 검사를 해야한다.

    # 왼쪽 윗 대각선 검사
    # row = 2, col = 2
    # range(2, -1, -1) -> (2, 1, 0) #위로 올라감
    # range(2, -1, -1) -> (2, 1, 0) #왼쪽으로 감
    # (2, 2), (1,1) , (0,)
    for i , j in zip(range(row,-1,-1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
        
    # 오른쪽 윗 대각선 검사
    # row = 2, col = 2
    # range(2, -1, -1) -> (2, 1, 0) #위로 올라감
    # range(2, 4) -> (2,3)
    for i,j in zip(range(row, -1,-1), range(col,n)):
        if board[i][j] == 1:
            return False
        
    return True


# row: 현재 퀸을 놓을 행
# board: 퀸들의 위치를 나타내는 n*n 보드
def n_queens(row, board):
    if row == n:
        # 그냥 완성된 체스판을 최종 결과에 저장
        solutions.append([r[:] for r in board])
        return


    # col = 0, 1, 2, 3 -> 행은 이미 row로 고정되어 있다.
    for col in range(n):
        # True 인 경우에는 놓을 수 있다.
        if is_valid_pos(board,row,col):
            # row에 해당하는 체스판에 퀸을 놨다.
            board[row][col] = 1
            # 다음 행으로 재귀 호출
            n_queens(row + 1,board)
            # 없었떤 일로 복구
            board[row][col] = 0


n = 4  # 4개의 퀸을 놓자 !
board = [[0] * n for _ in range(n)]  # 4*4 2차원 배열 생성
solutions = []  # 모든 솔루션을 저장할 리스트

'''
dfs
- 재귀를 종료할 변수 -> 각 행에 퀸을 놓을 수 있는지 확인하고, 마지막행까지 퀸을 전부 놨다면 끝!
- 우리가 원하는 누적값 -> 마지막 행까지 놓였을 때의 체스판 저장 상태를 원함.
'''

n_queens(0,board)

for solution in solutions:
    pprint.pprint(solution)
