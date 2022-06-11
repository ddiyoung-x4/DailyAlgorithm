from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    board = [[0]*101 for _ in range(101)]
    visited = [[0]*101 for _ in range(101)]
    
    for x1, y1, x2, y2 in rectangle:
        for i in range(2*x1, 2*x2+1):
            for j in range(2*y1, 2*y2+1):
                board[i][j] = 1
    
    for x1, y1, x2, y2 in rectangle:
        for i in range(2*x1+1, 2*x2):
            for j in range(2*y1+1, 2*y2):
                board[i][j] = 0
                
    root = [2*characterX, 2*characterY]
    q = deque([root])
    while q:
        x, y = q.popleft()
        
        if x == 2*itemX and y == 2*itemY:
            answer = board[x][y] // 2
            break
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= 101:
                continue
            elif ny < 0 or ny >= 101:
                continue
            if board[nx][ny] and not visited[nx][ny]:
                board[nx][ny] = board[x][y] + 1
                visited[nx][ny] = 1
                q.append([nx, ny])
    
    return answer