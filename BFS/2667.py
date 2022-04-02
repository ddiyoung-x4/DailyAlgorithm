import queue
import sys
input = sys.stdin.readline
  

N = int(input())

board = []
for i in range(N):
    board.append(list(map(int, input().strip())))

def bfs(root, N):
    visited = []
    queue = [root]
    cnt = 0

    while queue:
        pos_xy = queue[0]
        del queue[0]
        board[pos_xy[0]][pos_xy[1]] = -1

        if pos_xy not in visited:
            visited.append(pos_xy)
            dx = [-1, 0, 0, 1]
            dy = [0, -1, 1, 0]
            for j in range(4):
                new_x = pos_xy[0] + dx[j]
                new_y = pos_xy[1] + dy[j]

                if new_x < 0 or new_y < 0 or new_x >= N or new_y >= N:
                    continue
                
                if board[new_x][new_y] == 1:
                    queue.append([new_x, new_y])
        
    return len(visited)

total = 0
town_list = []
for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            total += 1
            town_list.append(bfs([i, j], N))

print(total)
town_list.sort()
for num in town_list:
    print(num)