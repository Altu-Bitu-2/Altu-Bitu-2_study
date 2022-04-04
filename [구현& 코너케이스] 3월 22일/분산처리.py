import sys

input = sys.stdin.readline

"""
[분산처리]

- a^b의 일의 자리를 구하는 문제
- 일의 자리는 0~9 중 하나 이므로, 어떤 수를 계속 곱해 나가면 일의 자리는 패턴을 가지게 되어 있음
    ex) 2 -> 4 -> 8 -> 6 -> 2 ... 
- 0~9까지 일의 자리 패턴을 미리 구한 후, (b % 패턴의 길이)번째 수를 출력하면 된다.
- 0이 나올 경우 10번 컴퓨터가 처리하므로, 0이 출력되지 않도록 예외처리
"""

last_digit = [[i] for i in range(10)]  # 0부터 9까지의 패턴
size = []  # 패턴의 길이

for i in range(10):     # 10대의 컴퓨터에 대해
    temp = i            # temp에 i번째 데이터가 몇번 컴퓨터를 사용하는지 저장
    while i != (temp * i) % 10: # temp에 i를 곱한 값의 일의 자리가 i가 아니면
        temp *= i
        temp %= 10      #temp의 일의자리 계산하여
        last_digit[i].append(temp)  # 패턴에 맞는 일의 자리 추가
    size.append(len(last_digit[i])) # 패턴 길이 추가

# 입력
t = int(input())

# 입력 + 연산
for _ in range(t):
    a, b = map(int, input().split())
    a %= 10     # a의 일의자리 계산

    if a == 0:      #10번 데이터는 10번 컴퓨터 출력
        print(10)
        continue

    print(last_digit[a][b % size[a] - 1])   # a의 패턴에서 b%길이 번째 수 출력