from collections import deque

n, k = map(int, input().split())

stack = deque([i for i in range(1, n+1)])
print("<", end="")
while len(stack) != 1:
    for _ in range(k-1):
        stack.append(stack.popleft())

    print(stack.popleft(), end=", ")
print(f"{stack.popleft()}>")