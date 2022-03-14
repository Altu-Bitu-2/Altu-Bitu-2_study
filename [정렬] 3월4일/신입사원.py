import sys

#테스트 케이스 한 줄 입력
T = int(input())

#테스트 케이스 수 만큼 시행
for i in range(0, T):
    cnt = 1
    people = [] #선발할 사람들

    N = int(input())
    #지원자 수만큼 성적을 공백 기준으로 매핑해서 저장
    for i in range(N):
        p, i = map(int, sys.stdin.readline().split())
        #선발 리스트에 두 성적 모두 필요하므로 리스트 형태로 정보 저장
        people.append([p, i])

    people.sort()  # 서류 기준 오름차순 정렬
    Max = people[0][1]  #그 다음 면접 순으로 오름차순 계산을 위해 기준값 설정

    #면접점수가 기준값보다 크면 그 사람은 선발 리스트에 추가하고 그 수만큼 cnt증가
    for i in range(1, N):
        if Max > people[i][1]:
            cnt += 1
            Max = people[i][1]

    print(cnt)

