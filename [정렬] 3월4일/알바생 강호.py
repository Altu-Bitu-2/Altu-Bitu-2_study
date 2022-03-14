# 팁 하나씩 입력받아
N = int(input())
data = []
# 리스트에 순서대로 저장
for _ in range(N) :
  data.append(int(input()))

# 손님 순서 변경
data.sort(reverse=True)

# 받을 팁 초기화
result = 0
#강호가 받을 돈 계산
for i in range(N):
  # 각 손님마다 계산된 돈 저장
  value = data[i] - ((i+1)-1)
  #계산값이 음수면 0원 처리, 양수 일때만 팁에 추가
  if value > 0 :
    result += value

print(result)