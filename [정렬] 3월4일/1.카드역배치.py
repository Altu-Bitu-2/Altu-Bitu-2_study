import sys

input = sys.stdin.readline()

arr = [i for i in range(0,20+1)]

def reverse(l,r):
    arr[l:r+1]=arr[r:l-1:-1]
    return

for i in range(10):
    a,b = map(int, input.split())
    reverse(a,b)
for i in arr[1:]:
    print(i,end="")