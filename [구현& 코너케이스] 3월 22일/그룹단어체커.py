import sys

input = sys.stdin.readline

"""
[그룹 단어 체커] - 단순 구현 문제

- 이미 등장한 알파벳 저장할 set() 선언 (탐색 O(1))
- 처음 등장하는 알파벳은 set에 추가하고, 무리에서 떨어졌는데 이미 등장한 알파벳이면 그룹 단어가 아니다.

"""


def is_group_word(word):
    checked = set()      #set()생성
    prev = None

    for c in word:      #단어에 특정 단어 체크
        if c == prev:   #전 알파벳이면 continue
            continue

        if c in checked:    #checked에 있는 알파벳이면 False리턴
            return False

        checked.add(c)
        prev = c        # 전 알파벳에 해당 단어 넣기

    return True


# 입력
n = int(input())

# 입력 + 연산
count = 0       #그룹 단어 세기

for _ in range(n):      #n번 반복
    word = input().rstrip()     #word에 해당 단어 넣기
    if is_group_word(word):     #그룹 단어에 있으면
        count += 1  #개수 추가

# 출력
print(count)        #그룹 단어 개수 출력