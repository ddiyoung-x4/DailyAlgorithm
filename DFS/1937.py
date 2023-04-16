import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

# DP + DFS 문제
# DFS만 사용시 시간초과

N = int(input())
board = [0] * N
for i in range(N):
    board[i] = list(map(int, input().split()))

di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]


answer = 1
# def dfs(i, j, visited, depth):
#     global answer
#     visited[i][j] = 1
#     answer = max(answer, depth)

#     for n in range(4):
#         ni = i + di[n]
#         nj = j + dj[n]
#         if 0 <= ni < N and 0 <= nj < N:
#             if not visited[ni][nj] and board[i][j] < board[ni][nj]:
#                 dfs(ni, nj, visited.copy(), depth+1)
dp = [[0] * N for _ in range(N)]
def dfs(i, j):
    if dp[i][j]:
        return dp[i][j]
    
    dp[i][j] = 1
    for n in range(4):
        ni = i + di[n]
        nj = j + dj[n]
        if 0 <= ni < N and 0 <= nj < N:
            if board[i][j] < board[ni][nj]:
                dp[i][j] = max(dp[i][j], dfs(ni, nj) + 1)
    
    return dp[i][j]

for i in range(N):
    for j in range(N):
        answer = max(answer, dfs(i, j))
print(answer)

