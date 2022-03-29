def bigsum(a, b):
    a = a[::-1]
    b = b[::-1]
    remain = 0
    result = []
    for i in range(len(a)):
        res = int(a[i]) + int(b[i]) + remain
        remain = res//10
        result.insert(0, str(res%10))
    if remain >= 1:
        result.insert(0, str(remain))
    return result

a, b = input().split()
print("".join(bigsum(a.zfill(max(len(a), len(b))), b.zfill(max(len(a),len(b))))))