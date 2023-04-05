from collections import deque

N, M = map(int, input().split())
r, c, d = map(int, input().split())

board = [0] * N
for i in range(N):
    board[i] = list(map(int, input().split()))

NOR = [-1, 0] # 0
EST = [0, 1] # 1 
SOT = [1, 0] # 2
WES = [0, -1] # 3
pole = [NOR, EST, SOT, WES]
visited = [[0] * M for i in range(N)]

def bfs(root, direction):
    q = deque([root])
    visited[root[0]][root[1]] = 1
    cnt = 1

    while q:
        n, m = q.popleft()
        flag = 0
        for i in range(4):
            new_n = n + pole[direction-1-i][0]
            new_m = m + pole[direction-1-i][1]
            if new_n >= 0 and new_n < N and new_m >= 0 and new_m < M:
                if not visited[new_n][new_m] and board[new_n][new_m] == 0:
                    flag += 1
                    cnt += 1
                    direction = direction-1-i
                    if direction < 0:
                        direction += 4
                    visited[new_n][new_m] = 1
                    q.append([new_n, new_m])
                    break

        # 후진    
        if flag == 0:
            flag = 0
            back_n = n + pole[direction-2][0]
            back_m = m + pole[direction-2][1]
            while board[back_n][back_m] != 1:
                for i in range(4):
                    new_n = back_n + pole[direction-i][0]
                    new_m = back_m + pole[direction-i][1]
                    if new_n >= 0 and new_n < N and new_m >= 0 and new_m < M:
                        if not visited[new_n][new_m] and board[new_n][new_m] == 0:
                            flag += 1
                            cnt += 1
                            direction = direction-i

                            if direction < 0:
                                direction += 4
                            visited[new_n][new_m] = 1
                            q.append([new_n, new_m])
                            break
                if flag > 0:
                    break
                back_n = back_n + pole[direction-2][0]
                back_m = back_m + pole[direction-2][1]
    return cnt
    
print(bfs([r,c], d))