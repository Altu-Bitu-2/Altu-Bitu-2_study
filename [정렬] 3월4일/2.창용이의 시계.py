import sys

# 한 줄 공백을 기준으로 시간 정보 맵핑
h, m, s = map(int, sys.stdin.readline().split())

# 쿼리 개수만큼 시간 계산
for _ in range(int(sys.stdin.readline())):
    # 쿼리 개수를 따지기 위해 리스트에 저장
    li = list(map(int, sys.stdin.readline().split()))
    # 아직 남아있는 쿼리가 3이면 출력
    if len(li) == 1 and li[0] == 3:
        print(h, m, s)
    # 아니면 이어서 계산
    else:
        # 범위를 갖는 시간단위 계산을 위해 시간을 초단위로 변환
        t = h*3600 + m*60 + s
        # 쿼리가 한개 남아있고 3이 아니면 그 쿼리 계산
        t += (li[1] if li[0] == 1 else -li[1])
        #계산한 초가 음수면 그만큼 원래 시간에 더해주고
        if t < 0:
            t += 86400
        # 아니면 기존 값으로 시간계산
        t = t%86400
        # 초 -> 시,분,초로 계산
        h, m, s = t//3600, (t%3600)//60, t%60