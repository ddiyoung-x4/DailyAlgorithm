N, M = map(int, input().split())

board = [0] * N
for i in range(N):
    board[i] = list(map(int, input().split()))
    
visited = [[0] * M for i in range(N)]

MaxValue = 0

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def dfs(i, j, SUM, cnt):
    global MaxValue

    if cnt == 4:
        MaxValue = max(MaxValue, SUM)
        return
    
    for n in range(4):
        new_n = i + dx[n]
        new_m = j + dy[n]
        if new_n >= 0 and new_n < N and new_m >= 0 and new_m < M:
            if not visited[new_n][new_m]:
                visited[new_n][new_m] = 1
                dfs(new_n, new_m, SUM + board[new_n][new_m], cnt+1)
                visited[new_n][new_m] = 0
    
# ㅗ, ㅜ, ㅏ, ㅓ 모양
def exce(i, j):
    global MaxValue
    for n in range(4):
        # 초기값은 시작지점의 값으로 지정
        tmp = board[i][j]
        for k in range(3):
            # 012, 123, 230, 301
            t = (n+k)%4
            ni = i+dx[t]
            nj = j+dy[t]

            if not (0 <= ni < N and 0 <= nj < M):
                tmp = 0
                break
            tmp += board[ni][nj]
        # 최대값 계산
        MaxValue = max(MaxValue, tmp)

for i in range(N):
    for j in range(M):
        # 시작점 visited 표시
        visited[i][j] = True
        dfs(i, j, board[i][j], 1)
        visited[i][j] = False
        exce(i, j)

print(MaxValue)