import sys

T = int(input())

for i in range(0, T):
    cnt = 1
    people = []

    N = int(input())
    for i in range(N):
        p, i = map(int, sys.stdin.readline().split())
        people.append([p, i])

    people.sort()  # 서류 기준 오름차순 정렬
    Max = people[0][1]

    for i in range(1, N):
        if Max > people[i][1]:
            cnt += 1
            Max = people[i][1]

    print(cnt)

