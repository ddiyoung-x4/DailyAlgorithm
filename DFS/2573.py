import sys
from collections import deque

dx = [-1,0,1,0]
dy = [0,-1,0,1]

def bfs(root):
    queue = deque([root])

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N:
                continue
            elif ny < 0 or ny >= M:
                continue

            if not visited[nx][ny] and board[nx][ny]:
                visited[nx][ny] = 1
                queue.append([nx,ny])
            elif board[nx][ny] == 0:
                count[x][y] += 1

N, M = map(int, input().split())

board = [[0]*M for _ in range(N)]
for i in range(N):
    board[i] = list(map(int, input().split()))

year = 0
cnt = 0
while 1:
    visited = [[0]*M for _ in range(N)]
    count = [[0]*M for _ in range(N)]
    cnt = 0

    for i in range(N):
        for j in range(M):
            if not visited[i][j] and board[i][j]:
                visited[i][j] = 1
                bfs([i,j])
                cnt += 1

    for i in range(N):
        for j in range(M):
            board[i][j] -= count[i][j]
            if board[i][j] < 0:
                board[i][j] = 0

    if cnt > 1:
        print(year)
        break
    elif cnt == 0:
        print(0)
        break
    year += 1