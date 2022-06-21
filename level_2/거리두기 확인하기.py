from collections import deque

def bfs(root, board):
    q = deque([root])
    
    visited = [[0]*5 for _ in range(5)]
    visited[root[0]][root[1]] = 1
    
    dx = [0, -1, 0, 1]
    dy = [-1, 0, 1, 0]
    
    while q:
        
        x, y = q.popleft()
        
        if visited[x][y] >= 4:
            return True
        
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if nx < 0 or nx >= 5:
                continue
            elif ny < 0 or ny >= 5:
                continue
            if board[nx][ny] != 'X' and not visited[nx][ny]:
                if board[nx][ny] == 'P' and visited[x][y] + 1 <= 3:
                    return False
                visited[nx][ny] += visited[x][y] + 1
                q.append([nx,ny])
    return True
def solution(places):
    answer = []
    
    for place in places:
        flag = True
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    flag = flag & bfs([i,j], place)
        if flag:
            answer.append(1)
        else:
            answer.append(0)
    return answer