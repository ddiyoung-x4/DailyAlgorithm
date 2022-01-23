import sys
N = int(sys.stdin.readline())
meeting = [0] * N
for i in range(N):
    meeting[i] = list(map(int, sys.stdin.readline().split()))

meeting = sorted(meeting, key=lambda x:x[0])
meeting = sorted(meeting, key=lambda x:x[1])

cnt = 1
finish = meeting[0][1]
for i in range(N-1):
    if finish <= meeting[i+1][0]:
        finish = meeting[i+1][1]
        cnt += 1
print(cnt)