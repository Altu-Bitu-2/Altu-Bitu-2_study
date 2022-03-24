import sys
N,M = map(int,input().split())

num =list(map(int,sys.stdin.readline().split()))

sum = 0
ans=[]

for i in range(len(num)-2):
    for j in range(i+1,len(num)-1):
        for k in range(j+1,len(num)):
            sum=num[i]+num[j]+num[k]
            if sum<=M:
                ans.append(sum)

print(max(ans))