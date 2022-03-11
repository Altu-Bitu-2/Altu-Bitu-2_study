N=int(input()) #점의 개수
arr=[]
for i in range(N): #점 좌표 받기
    a,b = map(int,input().split())
    arr.append((a,b))
arr.sort()
for i in range(N):
    print(arr[i][0],arr[i][1])