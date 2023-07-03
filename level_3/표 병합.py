from collections import deque

def merge(graph, board, r1, c1, r2, c2):
    
    graph[(r1, c1)] = graph.get((r1,c1), []) + [(r2,c2)]
    graph[(r2, c2)] = graph.get((r2,c2), []) + [(r1,c1)]
    
    if board[r1][c1] != 0 and board[r2][c2] != 0:
        value = board[r1][c1]
    elif board[r1][c1] != 0:
        value = board[r1][c1]
    elif board[r2][c2] != 0:
        value = board[r2][c2]
    else:
        value = 0
    board = update_value(graph, board, value, r1, c1)
    
    return graph, board

def update_value(graph, board, value, r, c):
    q = deque([(r,c)])
    visited = [(r,c)]
    
    while q:
        x, y = q.popleft()
        board[x][y] = value
        
        for new_r, new_c in graph[(x,y)]:
            if (new_r, new_c) not in visited:
                visited.append((new_r, new_c))
                q.append((new_r, new_c))
        
    return board

def unmerge(graph, board, value, r, c):
    q = deque([(r,c)])
    visited = [(r,c)]
    while q:
        x, y = q.popleft()

        board[x][y] = 0
        if (x,y) in graph.keys():
            for new_r, new_c in graph[(x,y)]:
                q.append((new_r, new_c))
        graph[(x, y)] = []
        del graph[(x,y)]
    board[r][c] = value
    
    return graph, board

def update_board(board, v1, v2):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == v1:
                board[i][j] = v2
    return board

def solution(commands):
    answer = []
    
    board = [[0] * 51 for i in range(51)]
    
    graph = {}
    
    for cmd in commands:
        cmd = cmd.split()
        if cmd[0] == 'UPDATE':
            if len(cmd) == 4:
                r, c, value = int(cmd[1]), int(cmd[2]), cmd[3]
                board[r][c] = value
                if (r, c) in graph:
                    board = update_value(graph, board, value, r, c)
            elif len(cmd) == 3:
                v1, v2 = cmd[1], cmd[2]
                board = update_board(board, v1, v2)
        elif cmd[0] == 'MERGE':
            r1, c1 = int(cmd[1]), int(cmd[2])
            r2, c2 = int(cmd[3]), int(cmd[4])
            graph, board = merge(graph, board, r1, c1, r2, c2)
        elif cmd[0] == 'UNMERGE':
            r, c = int(cmd[1]), int(cmd[2])
            graph, board = unmerge(graph, board, board[r][c], r, c)
        elif cmd[0] == 'PRINT':
            r, c = int(cmd[1]), int(cmd[2])
            if board[r][c] == 0:
                answer.append("EMPTY")
            else:
                answer.append(board[r][c])
    
    return answer