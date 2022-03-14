import sys

T = int(input())
N1= int(input())
li_1 = sys.stdin.readline().split()
N2 = int(input())
li_2 = sys.stdin.readline().split()

# li_2의 요소와 li_1요소 비교
for i in li_2:
    if i in li_1:
        print(1)
    else:
        print(0)