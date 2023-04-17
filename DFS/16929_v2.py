import sys
input = sys.stdin.readline

N, M = map(int, input().split())
board = [0] * N
for i in range(N):
    board[i] = list(input().rstrip())

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]

visited = [[0] * M for _ in range(N)]
answer = 'No'
def dfs(i, j, start, bi, bj):
    global answer
    if visited[i][j]:
        answer = 'Yes'
        return

    visited[i][j] = 1
    for n in range(4):
        ni = i + di[n]
        nj = j + dj[n]

        if not (0 <= ni < N and 0 <= nj < M) or board[i][j] != board[ni][nj]:
            continue
        if (ni, nj) == (bi, bj):
            continue
        dfs(ni, nj, start, i, j)

for i in range(N):
    for j in  range(M):
        if not visited[i][j]:
            dfs(i, j, [i, j], -1, -1)

        if answer == 'Yes':
            print(answer)
            sys.exit()
print(answer)