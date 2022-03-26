import sys

input = sys.stdin.readline

s = list(input().rstrip())[::-1]

#재귀함수 이용
def cal(start):
    r = 0 #개수 계산
    while s:
        a = s.pop()
        if a == "(" or a == "[":
            r += cal(a)
        elif start == "(" and a == ")":
            return 2 * max(1, r)
        elif start == "[" and a == "]":
            return 3 * max(1, r)

    # 리스트가 비었는데 최종 return 하지 못했다는 것은 괄호에 문제가 있음
    print(0)
    sys.exit()


ans = 0
while s:
    ans += cal(s.pop())
print(ans)