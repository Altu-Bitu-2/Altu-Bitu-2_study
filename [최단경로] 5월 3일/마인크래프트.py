import sys
input = sys.stdin.readline

INF = 10**9

"""
[마인크래프트]
 1. 가장 낮은 땅의 높이를 h라고 할 때, h-1의 높이를 만드는건 h보다 2*(N*M)의 시간이 더 소요됨
 2. 가장 높은 땅의 높이를 h라고 할 때, h+1의 높이를 만드는건 h보다 (N*M)의 시간이 더 소요됨
 -> 따라서 땅의 높이가 될 수 있는 후보는 (가장 낮은 땅) ~ (가장 높은 땅)
 -> 위치에 관계없이, 높이에 따라 필요한 블록 수와 시간이 결정되기 때문에 해당 높이의 블록이 몇 개 있는지 미리 저장 -> 가능한 높이 당 최대 256번의 연산만으로 계산 가능

 !주의! 당장 쌓을 블록이 없더라도 언젠가 다른 곳의 블록을 제거해서 쌓을 수 있음.
"""

def mine_land(min_height, max_height, b, height, cnt):      # 기존 높이와 비교해 만들 수 있는 최적의 높이 탐색
    t = 0       # 걸리는 시간
    for i in range(min_height, height):     # 가장 낮은 땅의 높이를 기준으로 기존 블록 개수와 시간 계산
        temp = cnt[i] * (height - i)
        b -= temp               #인벤토리 블록개수 1개 차감
        t += temp               # 걸리는 시간은 1번 시행마다 1초

    for i in range(height, max_height + 1):     # 가장 높은 땅의 높이를 기준으로 기존 블록 개수와 시간 계산
        temp = cnt[i] * (i - height)
        b += temp               #인벤토리 블록개수 1개 추가
        t += temp * 2           # 걸리는 시간은 1번 시행마다 2초

    if b < 0:                   #만약 인벤토리 블록이 더 이상 없으면
        return INF + 1          #종료

    return t                    #걸린 시간 반환


# 입력
n, m, b = map(int, input().split())

cnt = [0]*257   # cnt[i] = 높이 i를 가지고 있는 땅의 수
min_height = 256    # 초기화시 가장 높은 땅의 높이는 최대 256
max_height = 0      # 초기화시 가장 낮은 땅의 높이는 최소 0

for _ in range(n):  # 땅의 높이 입력 받는 for문
    for i in map(int, input().split()):
        cnt[i] += 1
        min_height = min(min_height, i) #최대값 찾기
        max_height = max(max_height, i) #최솟값 찾기

min_t = INF # 더 이상 블록이 존재하지 않았을 때까지 걸린 시간
height = 0

# 연산
for h in range(min_height, max_height+1):
    t = mine_land(min_height, max_height, b, h, cnt)    # 시간계산하는 함수에서 리턴한 값 저장
    if t <= min_t:  # 인밴토리 블록 수가 없어서 종료된 시간과 최소 시간 비교
       min_t = t
        height = h

# 출력
print(min_t, height)