#모듈 가져오기
import sys

#한 줄에 여러 값을 한 변수로 처리
input = sys.stdin.readline()

#카드 위치 계산을 위한 배열
arr = [i for i in range(0,20+1)]

#역순으로 바꿀 카드 범위를 받아 역순(-1)으로 하여 구간 순서 바꿈
def reverse(l,r):
    arr[l:r+1]=arr[r:l-1:-1]
    return

# 입력 받은 10가지를 같은 방식으로 for문으로 반복 계산
for i in range(10):
    # 한 줄에 공백을 기준으로 두 변수에 맵핑
    a,b = map(int, input.split())
    #위 함수에 넣어 계산된 값 반환
    reverse(a,b)
# 계산 다 된 arr리스트 원소 가져오기
for i in arr[1:]:
    print(i,end="")