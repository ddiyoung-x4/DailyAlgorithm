from collections import deque

N, M = map(int, input().split())
r, c, d = map(int, input().split())

board = [0] * N
for i in range(N):
    board[i] = list(map(int, input().split()))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

visited = [[0] * M for i in range(N)]

def bfs(root, direction):
    q = deque([root])
    visited[root[0]][root[1]] = 1
    cnt = 1

    while q:
        n, m = q.popleft()
        flag = 0
        for i in range(4):
            direction = (direction + 3) % 4
            new_n = n + dx[direction]
            new_m = m + dy[direction]
            if new_n >= 0 and new_n < N and new_m >= 0 and new_m < M:
                if not visited[new_n][new_m] and board[new_n][new_m] == 0:
                    flag += 1
                    cnt += 1
                    visited[new_n][new_m] = 1
                    q.append([new_n, new_m])
                    break

        # 후진    
        if flag == 0:
            if board[n - dx[direction]][m - dy[direction]] == 1:
                break
            else:
                q.append([n -dx[direction], m - dy[direction]])
    return cnt
    
print(bfs([r,c], d))