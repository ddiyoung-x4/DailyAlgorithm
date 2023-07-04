def solution(board, skill):
    answer = 0
    N = len(board)
    M = len(board[0])
    prefix_sum = [[0] * (M+1) for i in range(N+1)]

    for t, r1, c1, r2, c2, degree in skill:
        t_degree = degree * (-1) if t == 1 else degree
        prefix_sum[r1][c1] += t_degree
        prefix_sum[r2+1][c1] -= t_degree
        prefix_sum[r1][c2+1] -= t_degree
        prefix_sum[r2+1][c2+1] += t_degree
    
    for i in range(N+1):
        for j in range(1, M+1):
            prefix_sum[i][j] += prefix_sum[i][j-1]
    
    for j in range(M+1):
        for i in range(1, N+1):
            prefix_sum[i][j] += prefix_sum[i-1][j]

    for i in range(N):
        for j in range(M):
            board[i][j] += prefix_sum[i][j]
            if board[i][j] > 0:
                answer += 1
    return answer