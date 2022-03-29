import sys
input = sys.stdin.readline

"""
[집합] - 단순 구현 문제

ver1. 리스트 사용
set()을 사용해서 매번 연산을 하면 시간이 굉장히 오래 걸려요.
입력되는 x의 값이 1~20으로 범위가 매우 작기 때문에, 각 숫자가 집합에 들어있는 여부를 저장하는 리스트를 이용합니다.

1. 크기가 21인 리스트 선언
2. add는 True, remove는 false

"""
SIZE = 21
m = int(input())
s = [False]*SIZE
value = {"all":True, "empty":False}

def update(cmd):        # cmd값으로 모든 s를 값을 바꿔줌
    for i in range(1, 21):
        s[i] = value[cmd]

def check(num):     # 만약 s[num]이 True이면 1,아니면 0리턴
    if s[num]:
        return 1
    return 0

for _ in range(m):          # m번 만큼 반복하여
    cmd = input().split()    # [0]은 연산, [1]은 숫자

    if len(cmd) == 1:       # cmd길이가 1이면 update
        update(cmd[0])
        continue
    else:
        num = int(cmd[1])       #다른 연산이면 num에 [1]의 정수형 넣음
    if cmd[0] == "add":         #add연산이면
        s[num] = True           #s[num]을 True로
    elif cmd[0] == "remove":    #remove연산이면
        s[num] = False          #s[num]을 False
    elif cmd[0] == "check":     #check연산이면
        print(check(num))       #check값 출력
    elif cmd[0] == "toggle":    #toggle연산이면
        s[num] = not s[num]     #s의 값 바꾸기