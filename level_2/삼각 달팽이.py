def solution(n):
    answer = []
    board = [[0] * n for _ in range(n)]

    def go_down(pos, n):
        x, y = pos
        for i in range(n):
            board[x+i+1][y] = board[x+i][y] + 1

        return [x+n, y]

    def go_right(pos, n):
        x, y = pos
        for j in range(n):
            board[x][y+j+1] = board[x][y+j] + 1

        return [x, y+n]

    def go_left_up(pos, n):
        x, y = pos
        for i in range(n):
            board[x-i-1][y-i-1] = board[x-i][y-i] + 1

        return [x-n, y-n]    
    # d -> r -> l,u -> d -> r -> l, u
    board[0][0] = 1
    pos = go_down([0,0], n-1)
    flag = 0
    for k in range(n-1, 0, -1):
        if flag == 0:
            pos = go_right(pos, k)
        elif flag == 1:
            pos = go_left_up(pos, k)
        else:
            pos = go_down(pos, k)
        flag += 1
        flag %= 3
    
    for i in range(n):
        for j in range(n):
            if board[i][j]:
                answer.append(board[i][j])
            else:
                break
    return answer