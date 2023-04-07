N, M, R = map(int, input().split())

board = [0] * N
for i in range(N):
    board[i] = list(map(int, input().split()))

for _ in range(R):
    for i in range(min(N, M) // 2):
        x, y = i, i
        temp = board[x][y]

        # 아래로 내려가는 경우
        for j in range(i+1, N - i):
            x = j
            prev = board[x][y]
            board[x][y] = temp
            temp = prev
        
        # 오른쪽 이동
        for j in range(i+1, M-i):
            y = j
            prev = board[x][y]
            board[x][y] = temp
            temp = prev

        # 위로 이동
        for j in range(i+1, N-i):
            x = N - j - 1
            prev = board[x][y]
            board[x][y] = temp
            temp = prev

        # 왼쪽 이동
        for j in range(i+1, M-i):
            y = M - j - 1
            prev = board[x][y]
            board[x][y] = temp
            temp = prev

for i in range(N):
    for j in range(M):
        print(board[i][j], end=' ')
    print()