import sys
input = sys.stdin.readline

W, N = map(int, input().split())
m = [[0, 0] for i in range(N)]
for i in range(N):
    m[i][0], m[i][1] = map(int, input().split())

m.sort(key=lambda x: x[1], reverse=True)

answer = 0
for i in range(N):
    if W - m[i][0] > 0:
        W -= m[i][0]
        answer += m[i][0] * m[i][1]
    else:
        answer += W * m[i][1]
        break

print(answer)