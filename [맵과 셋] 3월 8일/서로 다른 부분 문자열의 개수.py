import sys

s = input()

# 중복되지 않는 문자열만 따지므로 set자료형 사용
ans = set()
n = len(s)

for i in range(0,n+1):
    for j in range(i,n):
            ans.add(s[i:j+1])
print(len(ans))

