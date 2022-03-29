L, C = map(int, input().split())
s = sorted(list(input().split()))
vowel = ["a", "e", "i", "o", "u"]


def bt(cnt, pw, idx):
    if not cnt:
        tmp = pw
        # 모음을 제거한다.
        for i in vowel:
            if i in pw:
                pw = pw.replace(i, "")
        # pw의 길이가 2 이상이면 자음이 2개 이상이고, l보다 작다면 모음이 1개 이상 포함되는 것이다.
        if L > len(pw) > 1:
            print(tmp)
        return

    for i in range(idx, C - cnt + 1):
        bt(cnt - 1, pw + s[i], i + 1)


bt(L, "", 0)