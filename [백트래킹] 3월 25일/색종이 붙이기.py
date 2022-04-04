import sys

input = sys.stdin.readline

"""
1. 붙일 수 있는 색종이의 최소 개수를 구하는 것이므로, 큰 색종이부터 붙여가면서 세어보아야 함
2. 색종이의 개수가 각 5장씩으로 제한되어 있기 때문에, 사용한 색종이의 개수를 기록해야 함
"""

SIZE = 10
MAX = 26


# (r, c)부터 시작해서 paper_size크기의 색종이를 붙일 수 있는지 확인하는 함수
def promising(r, c, paper_size):
    for i in range(r, r + paper_size):
        for j in range(c, c + paper_size):
            if board[i][j] == 0: #만약 0이 발견되면 그 뒤 색종이 못씀
                return False
    return True

#그래프 색칠하기
# board의 (r, c)부터 시작해서 paper_size크기를 num으로 채우는 함수
def fill_board(r, c, paper_size, num): #num아 0아면 색종이 붙이고 1이면 색종이 떼는 로직
    for i in range(r, r + paper_size):
        for j in range(c, c + paper_size):
            board[i][j] = num
    return

#백트래킹 탐색
def backtracking(idx, count):
    global answer  # 전역변수 사용

    if count > answer:
        return

    if idx == SIZE * SIZE: #덮어야 할 곳 모두 덮은 경우
        answer = min(answer, count)
        return

    x, y = idx // SIZE, idx % SIZE  # x행 y열

    if board[x][y] == 0:  # 현재 칸이 0이라면 넘어감
        backtracking(idx + 1, count)
        return

    for i in range(5, 0, -1): #5부터 1까지
        if x + i > SIZE or y + i > SIZE: #색종이가 떨어지지 않았고 해당 색종이를 붙일 범위가 존재하면
            continue
        if promising(x, y, i) and paper_cnt[i] > 0: #색종이가 있으면 붙이고 재귀
            paper_cnt[i] -= 1   #사용한 색종이 제거
            fill_board(x, y, i, 0) # 커버해야 할 좌표 0으로 커버
            backtracking(idx + i, count + 1) #완전 탐색 다시 시작
            paper_cnt[i] += 1 #사용한 색종이 추가
            fill_board(x, y, i, 1) # 백트래킹에서 다시 돌아왔으면 다시 1로 돌려줌

    return


# 입력
board = [list(map(int, input().split())) for _ in range(SIZE)]

paper_cnt = [5] * 6  # 남은 색종이의 수 (index 1~5 사용)
answer = MAX  # 최솟값 갱신할 변수

# 연산
backtracking(0, 0)

if answer == MAX:  # 불가한 경우
    print(-1)
else:
    print(answer)