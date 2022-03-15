N=int(input()) #점의 개수
arr=[]

#입력 받은 점 좌표 리스트에 순차적으로 저장
for i in range(N):
    # x,y좌표에 매핑
    a,b = map(int,input().split())
    # 좌표이므로 튜플 형태로 리스트에 저장
    arr.append((a,b))
# 정렬
arr.sort()
# 리스트에 튜플이 원소인 값 추출
for i in range(N):
    print(arr[i][0],arr[i][1])