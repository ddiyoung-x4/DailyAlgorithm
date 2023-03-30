import sys
input = sys.stdin.readline

dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]
def bfs(start, board):
    cnt = 1
    q = [[start[0], start[1]]]
    while q:
        m, n = q.pop()
        for i in range(4):
            next_m, next_n = m + dx[i], n + dy[i]
            if next_m < N and next_m >= 0 and next_n < N and next_n >= 0:
                if not visited[next_m][next_n] and board[next_m][next_n] == '1':
                    cnt += 1
                    visited[next_m][next_n] = 1
                    q.append([next_m, next_n])
    return cnt

N = int(input())
board = [0] * N
for i in range(N):
    board[i] = input().rstrip()

visited = [[0] * N for i in range(N)]

answer = []
block_cnt = 0
for i in range(N):
    for j in range(N):
        if board[i][j] == '1' and not visited[i][j]:
            block_cnt += 1
            visited[i][j] = 1
            answer.append(bfs([i, j], board))
answer.sort()
print(block_cnt)
for ans in answer:
    print(ans)