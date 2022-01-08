import math
S = input()

cnt1, cnt2 = 0, 0
ch = S[0]
for i in range(1, len(S)):
    if ch != S[i]:
        cnt1 += 1
        ch = S[i]

print(math.ceil(cnt1/2))
