import sys
from collections import deque

input = sys.stdin.readline

"""
[Puyo Puyo] - bfs, 시뮬레이션 문제

1. bfs 탐색을 통해 4개 이상의 뿌요가 모였는지 확인
2. 4개 이상의 뿌요가 모였다면, 해당되는 영역을 '.'으로 바꾸어 비워줌
3. 전체 필드에 대해 1~2를 다 수행한 후, 뿌요를 떨어뜨림
    - 바닥부터 시작해서 남아있는 뿌요들을 모으고, 남은 부분은 '.'으로 채우는 방식
4. 터뜨릴 수 없을 때까지 반복

여기서, 3번 과정을 편하게 하기 위해 12*6으로 들어오는 입력을 6*12로 바꾸어준다.
같은 열에 있는 데이터를 다루는 것보다 같은 행에 있는 데이터를 다루는 것이 편하기 때문이다.
"""

# 행과 열을 바꾸어 사용하므로 ROW를 6, COL은 12로 설정
ROW = 6
COL = 12

#뭉쳐져 있는 뿌요 그룹 찾는 함수
def bfs(i, j):
    dr = [-1, +1, 0, 0]
    dc = [0, 0, -1, +1]
    que = deque()

    que.append((i, j))
    visited = [[False] * COL for _ in range(ROW)]   # 경로 탐색, 방문하지 않은 장소는 False로 초기화
    visited[i][j] = True    # 방문장소는 True로 변경
    color = board[i][j] #색깔 뿌요
    count = 1  # 모여있는 뿌요의 개수
    cords = []  # 포함된 좌표 저장할 리스트

    while que:
        cords.append(que[0])
        r, c = que.popleft()
        for x in range(4):
            nr, nc = r + dr[x], c + dc[x]
            if not (0 <= nr < ROW and 0 <= nc < COL):   #범위 밖일 경우 pass
                continue
            if not visited[nr][nc] and board[nr][nc] == color:   #탐색 중인 칸의 뿌요 색이 현재 탐색기준 뿌요 색과 동일하고, 방문한 적이 없을 때
                visited[nr][nc] = True  #다음 탐색 대상 좌표 추가, 방문 처리
                que.append((nr, nc))      #뿌요 그룹 리스트에 추가
                count += 1

    if count < 4:   #연쇄가 일어나는 그룹 없는 경우
        return False

    for r, c in cords:  #연쇄가 일어나는 그룹 있는 경우
        board[r][c] = '.'

    return True


# 뿌요를 터뜨린 이후의 새 필드를 작성하는 함수
def make_new_board(board):
    new_board = []
    for i in range(ROW):
        temp = []
        for j in range(COL):    #뿌요 그룹을 삭제하고, 뿌요들을 내려주기
            # 남아있는 뿌요를 임시 리스트에 모으기
            if board[i][j] != '.':
                temp.append(board[i][j])
        # 비어 있는 부분을 '.'로 채우기
        while len(temp) < COL:
            temp.append('.')
        new_board.append(temp[:])
    return new_board


# 입력
board = [[None] * COL for _ in range(ROW)]

# 행과 열을 바꾸어 저장
for i in range(COL):
    line = input().rstrip()
    for j in range(ROW):
        board[j][12 - i - 1] = line[j]

ans = 0

while True:
    flag = False
    for i in range(ROW):
        for j in range(COL):
            if board[i][j] == '.':   #칸이 '.'로 뿌요가 없을 시 pass
                continue
            if bfs(i, j):
                flag = True

    if not flag:     #삭제할 뿌요가 없을 때
        break
    ans += 1    #연쇄 횟수 1회 추가
    board = make_new_board(board)   #삭제할 뿌요가 있을 때 뿌요 삭제 후 이동 함수를 통해 처리 후의 뿌요 필드를 반환받음

print(ans)