import sys
input = sys.stdin.readline

M, N = map(int, input().split())
grid = []

tomato_1 = []
for i in range(N):
    grid.append(list(map(int, input().strip().split())))
    for j in range(M):
        if grid[i][j] == 1:
            tomato_1.append([i, j])

def bfs(not_raw):
    visited = []
    queue = not_raw
    dist = 0

    while queue:
        pos_xy = queue[0]
        del queue[0]

        if pos_xy not in visited:
            dx = [-1, 0, 0, 1]
            dy = [0, -1, 1, 0]
            for i in range(4):
                new_x = pos_xy[0] + dx[i]
                new_y = pos_xy[1] + dy[i]

                if new_x < 0 or new_y < 0 or new_x >= N or new_y >= M:
                    continue
                if grid[new_x][new_y] == 0:
                    queue.append([new_x, new_y])
                    grid[new_x][new_y] = grid[pos_xy[0]][pos_xy[1]] + 1
                    dist = grid[new_x][new_y]
    return dist
dist = bfs(tomato_1)


for i in range(N):
    if 0 in grid[i]:
        print(-1)
        sys.exit()

if dist:
    print(dist)
else:
    print(0)