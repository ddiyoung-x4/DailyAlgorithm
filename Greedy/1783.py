import sys

N, M = map(int, sys.stdin.readline().split())

answer = 0
if N >= 3 and M >= 7:
    answer = M - 6 + 4
else:
    # N < 3 or M < 7
    if N < 3:
        if N == 1:
            answer = 1
        else:
            answer = min(4, M // 2 + M % 2)
    elif M < 7:
        # N >= 3 인 경우
        answer = min(4, M)
print(answer)
