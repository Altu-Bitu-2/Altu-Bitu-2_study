import sys
import heapq as hq

input = sys.stdin.readline

"""
[해킹]
- 기본적인 다익스트라 문제
- 우선순위 큐에 삽입을 할 때는 이후 더 빠른 시간이 큐에 들어올 가능성이 있으므로 삽입할 때는 표기하지 않고, 큐에서 제거하는 시점에서 방문 표기 (큐에서 제거하는 시점에는 그때의 시간이 이후로 등장할 수 있는 가장 빠른시간이다.)

 !주의! 그래프 생성 시, a가 b를 의존한다는 건 b 감염 후 a가 감염된다는 뜻이므로 b -> a 방향임
"""


def dijkstra(n, c, graph):
    visited = [False] * (n + 1) # 방문하지 않은 요소 False처리

    pq = [(0, c)]    #우선 순위 큐에 [최단 시간, 노드] 추가

    t = 0       # 시작 지점은 0으로 초기화
    cnt = 0

    while pq:
        curr_t, curr = hq.heappop(pq)   # 가장 빠른 시간 pop
        if visited[curr]:    #이미 time 에 최단 시간이 저장된 경우 패스
            continue
        visited[curr] = True    # 업데이트
        t = curr_t
        cnt += 1
        for next, weight in graph[curr]:    # 연결된 노드 확인
            if not visited[next]:
                hq.heappush(pq, (t + weight, next)) # 업데이트가 된 노드는 다시 우선 순위 큐에 저장

    return cnt, t


# 입력
t = int(input())

for _ in range(t):
    # 입력
    n, d, c = map(int, input().split())
    graph = [[] for _ in range(n + 1)]

    # 인접 리스트로 저장
    for _ in range(d):
        a, b, s = map(int, input().split())
        graph[b].append((a, s))

    # 연산 + 출력
    print(*dijkstra(n, c, graph))