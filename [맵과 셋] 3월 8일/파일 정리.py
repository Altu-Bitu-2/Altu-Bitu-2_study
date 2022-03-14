from collections import Counter #리스트 요소별 개수를 딕셔너리로 반환해주는 컬렉션

n = int(input())
# 한 줄에 받은 입력값을 리스트 요소로 넣는 방법
s = list(input() for _ in range(n))
# 파일 확장자별 개수 저장 리스트
cnt=[]

for word in s:
    cnt.append(word.split('.')[1])
cnt=sorted(cnt)

counter = Counter(cnt)

# 확장자-개수 딕셔너리 키,값 모두 출력
for k,v in dict(counter).items():
    print(k,v)






