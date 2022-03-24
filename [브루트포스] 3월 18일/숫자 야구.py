import sys
ans = [True]*1000
N = int(sys.stdin.readline())
cnt = 0
for n in range(N):
    num, s, b = map(int, sys.stdin.readline().split())
    num = str(num)
    for i in range(123, 988):
        i = str(i)
        if i[0] == i[1] or i[0] == i[2] or i[1] == i[2]:
            ans[int(i)] = False
        if i[0] == '0' or i[1] == '0' or i[2] == '0':
            ans[int(i)] = False
        s_cnt = 0
        b_cnt = 0
        for j in range(3):
            for k in range(3):
                if i[j] == num[k]:
                    if j == k:
                        s_cnt += 1
                    else:
                        b_cnt += 1
        if ans[int(i)] and s_cnt == s and b_cnt == b:
            ans[int(i)] = True
        else:
            ans[int(i)] = False
for i in range(123, 988):
    if ans[i]:
        cnt += 1
print(cnt)
