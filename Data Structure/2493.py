import sys
N = int(sys.stdin.readline())
tower = list(map(int, sys.stdin.readline().split()))
answer = [0] * N
tmp = [[0, 0]]
for i in range(1, N):
    if tower[i-1] > tower[i]:
        tmp.append([tower[i-1], i-1])
        answer[i] = i
    else:
        if tmp[-1][0] > tower[i]:
            answer[i] = tmp[-1][1]+1
        else:
            while len(tmp) and tmp[-1][0] < tower[i]:
                tmp.pop()
            if len(tmp):
                answer[i] = tmp[-1][1]+1
            else:
                tmp.append([tower[i], i])

for i in range(len(answer)):
    print(answer[i], end=' ')