N = int(input())
data = []
for _ in range(N) :
  data.append(int(input()))

data.sort(reverse=True)

result = 0
for i in range(N) :
  value = data[i] - ((i+1)-1)
  if value > 0 :
    result += value

print(result)