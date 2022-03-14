import sys

s = input()

# 중복되지 않는 문자열만 따지므로 set자료형 사용
ans = set()
n = len(s)

for i in range(n):
    for j in range(n-1):
        if s[i:j+2] !='':
            ans.add(s[i:j+2])
print(ans)

