import sys
input = sys.stdin.readline
# python recursion 깊이 제한(1000) 때문에 필수
sys.setrecursionlimit(10**6)

dx = [-1,0,1,0]
dy = [0,-1,0,1]

def dfs(x, y):
    if x == N-1 and y == M-1:
        return 1
    if visited[x][y] != -1:
        return visited[x][y]
    visited[x][y] = 0
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if nx < 0 or nx >= N:
            continue
        elif ny < 0 or ny >= M:
            continue
        if board[nx][ny] < board[x][y]:
            visited[x][y] += dfs(nx, ny)
    return visited[x][y]
    
N, M = map(int, input().split())
board = [[0]*M for _ in range(N)]
visited = [[-1]*M for _ in range(N)]
for i in range(N):
    board[i] = list(map(int, input().split()))
print(dfs(0, 0))