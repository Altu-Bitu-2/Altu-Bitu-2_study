r,b = map(int,input().split())
for i in range(3,3000):
    for j in range(3,3000):
        if i*2+2*(j-2)==r and (i-2)*(j-2)==b:
            L,W = i,j
            break
if L<W:
    W,L = L,W
print(L,W)