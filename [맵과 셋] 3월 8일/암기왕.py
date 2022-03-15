import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N1 = int(input())
    li_1 = set(map(int,input().split()))
    N2 = int(input())
    li_2 = list(map(int,input().split()))

# li_2의 요소와 li_1요소 비교
for i in li_2:
    if i in li_1:
        print(1)
    else:
        print(0)


