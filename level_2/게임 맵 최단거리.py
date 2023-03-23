def solution(maps):
    answer = 0
    
    answer = bfs(maps)
    
    return answer

def bfs(maps):
    n = len(maps)
    m = len(maps[0])
    q = [[0, 0]]
    visited = [[0] * m for i in range(n)]
    visited[0][0] = 1
    
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    
    while q:
        x, y = q.pop(0)
        for i in range(4):
            new_x = x + dx[i]
            new_y = y + dy[i]
            if new_x >= 0 and new_x < n and new_y >= 0 and new_y < m:
                if maps[new_x][new_y] and not visited[new_x][new_y]:
                    visited[new_x][new_y] = visited[x][y] + 1
                    q.append([new_x, new_y])
    if visited[-1][-1] == 0:
        return -1
    
    return visited[-1][-1]