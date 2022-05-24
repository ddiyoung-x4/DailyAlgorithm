from collections import deque

def make_board(X, Y, check_list):
    board = [[0]*Y for _ in range(X)]
    for x, y in check_list:
        board[x][y] = 1
    
    return board


def rotate90(board):
    X = len(board)
    Y = len(board[0])
    new_board = [[0]*X for _ in range(Y)]
    for i in range(X):
        for j in range(Y):
            new_board[j][X-1-i] = board[i][j]
    return new_board

def is_same_board(board1, board2):
    for i in range(4):
        if board1 == board2:
            return True
        else:
            board2 = rotate90(board2)
    return False

def solution(game_board, table):
    
    answer = 0
    N = len(game_board)
    visited = [[0]* N for _ in range(N)]
    for d in game_board:
        print(d)
    print('-------------')
    def bfs(x, y, board, flag):
        visited[x][y] = 1
        queue = deque([[x,y]])
        block = [[x, y]]

        dx = [0, -1, 0, 1]
        dy = [-1, 0, 1, 0]
        while queue:
            x, y = queue.popleft()

            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if nx < 0 or nx >= N:
                    continue
                elif ny < 0 or ny >= N:
                    continue
                if not visited[nx][ny] and board[nx][ny] == flag:
                    queue.append([nx,ny])
                    visited[nx][ny] = 1
                    block.append([nx,ny])

        block = sorted(block, key=lambda x:x[0])
        min_x = block[0][0]
        max_x = block[-1][0]
        block = sorted(block, key=lambda x:x[1])
        min_y = block[0][1]
        max_y = block[-1][1]
        len_x = max_x - min_x
        len_y = max_y - min_y
        for i in range(len(block)):
            block[i] = [block[i][0] - min_x, block[i][1] - min_y]
            
        return len_x+1, len_y+1, block

    block_list = []
    for i in range(N):
        for j in range(N):
            if game_board[i][j] == 0 and not visited[i][j]:
                block_list.append(bfs(i, j, game_board, 0))
    
        
    puzzle_list = []
    visited = [[0]* N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if table[i][j] == 1 and not visited[i][j]:
                puzzle_list.append(bfs(i, j, table, 1))
    # for d in puzzle_list:
    #     print(d)
    
    for b_len_x, b_len_y, block in block_list:
        block_board = make_board(b_len_x, b_len_y, block)
        # print('block_board')
        # for d in block_board:
        #     print(d)
        for idx, (p_len_x, p_len_y, puzzle) in enumerate(puzzle_list):
            # print('eeeee', b_len_x, b_len_y, p_len_x, p_len_y)
            if not (b_len_x == p_len_x and b_len_y == p_len_y) and \
                not (b_len_x == p_len_y and b_len_y == p_len_x):
                continue
            else:
                puz_board = make_board(p_len_x, p_len_y, puzzle)
                # print('puz_board')
                # for d in puz_board:
                #     print(d)
                if is_same_board(block_board, puz_board):
                    
                    print(len(puzzle))
                    answer += len(puzzle)
                    puzzle_list.pop(idx)
                    break

    return answer