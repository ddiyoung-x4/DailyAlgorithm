T = int(input())

for i in range(T):
    M, N, K = map(int, input().split())
    board = [[0]*N for _ in range(M)]
    for j in range(K):
        a, b = map(int, input().split())
        board[a][b] = 1
    
    cnt = 0
    for k in range(M):
        for l in range(N):
            if board[k][l] == 1:
                q = [[k, l]]
                while q:
                    a = q[0][0]
                    b = q[0][1]
                    board[a][b] = 0 # 1인 값중에 visit이면 0
                    del q[0]

                    if a + 1 < M and board[a+1][b] == 1: # 아래
                        board[a+1][b] = 0
                        q.append([a+1, b])
                    if 0 <= a - 1 and board[a-1][b] == 1: # 위
                        board[a-1][b] = 0
                        q.append([a-1, b])
                    if b + 1 < N and board[a][b+1] == 1: # 오른
                        board[a][b+1] = 0
                        q.append([a, b+1])
                    if 0 <= b - 1 and board[a][b-1] == 1: # 왼
                        board[a][b-1] = 0
                        q.append([a, b-1])
                cnt += 1
    print(cnt)