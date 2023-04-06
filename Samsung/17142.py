from collections import deque

N, M = map(int, input().split())

board = [0] * N
virus = []
for i in range(N):
    board[i] = list(map(int, input().split()))
    for j in range(N):
        if board[i][j] == 2:
            virus.append([i, j])

MinValue = N * N
# dfs를 통해 combinations 구현
def dfs(q, depth):
    global MinValue
    if len(q) == M:
        # virus M개 선택 후
        # print(q)
        visited = [[-1] * N for _ in range(N)]
        for i, j in q:
            visited[i][j] = 0
        queue = q.copy()
        result = bfs(queue, visited)
        if result >= 0:
            MinValue = min(MinValue, result)
        return
    
    elif depth == len(virus):
        return
    
    q.append(virus[depth])
    dfs(q, depth+1)
    q.pop()
    dfs(q, depth+1)

def bfs(q, visited):

    dn = [0, 1, 0, -1]
    dm = [1, 0, -1, 0]
    MAX = 0

    while q:
        i, j = q.popleft()

        for k in range(4):
            ni = i + dn[k]
            nj = j + dm[k]
            if 0 <= ni < N and 0 <= nj < N:
                if visited[ni][nj] < 0 and (board[ni][nj] == 0 or board[ni][nj] == 2):
                    visited[ni][nj] = visited[i][j] + 1
                    q.append([ni, nj])
    for i in range(N):
        for j in range(N):
            if board[i][j] == 0 and visited[i][j] < 0:
                return -1
            elif board[i][j] == 0 and visited[i][j] > 0:
                MAX = max(MAX, visited[i][j])
    return MAX

dfs(deque(), 0)
if MinValue == N * N:
    print(-1)
else:
    print(MinValue)