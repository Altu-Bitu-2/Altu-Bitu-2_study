import sys

input = sys.stdin.readline

"""
 1. 우선 수열을 사전 순으로 증가하는 순서로 출력해야 하므로 주어진 수열을 오름차순 정렬
 2. 이 상태에서 우선, 같은 위치의 수를 또 선택하지 않도록 중복제거 (check 배열 사용)를 해줌
 3. 그 후, 중복되는 "수열"을 거르는 방법은 이전에 선택한 값을 변수에 저장해서, 수열을 만들다 다시 루트 노드로 돌아왔을 때
    이전에 선택한 값과 같은 값이면 넘어가면 됨! -> 어차피 같은 수이므로 같은 과정 반복해서 똑같은 수열이 나올 것
"""


def backtracking(idx, m):
    if idx == m: #만약 m개를 골랐다면 출력
        print(*answer)  # *list -> 리스트의 요소를 하나씩 풀어서 print()에 인자로 넣어줌
        # print(*[1, 2, 3]) == print(1, 2, 3)
        return

    prev = 0  # 이전에 선택한 값
    for i in range(n):
        if not checked[i] and arr[i] != prev: #직전에 골랐던 수가 아니고 이미 고른 수가 아니면
            checked[i] = True #골라주고
            prev = arr[i]   #배열에 넣고
            answer[idx] = arr[i] #직전 고른 수에 저장
            backtracking(idx + 1, m) #다음수를 고르러 감
            checked[i] = False

    return


n, m = map(int, input().split()) #한 줄에 여러 값-> map이용
arr = list(map(int, input().split()))
arr.sort() # 수열은 사전 순으로 출력해야 하므로 입력 받고 오름차순으로 정렬
checked = [False] * n
answer = [0] * m

backtracking(0, m)