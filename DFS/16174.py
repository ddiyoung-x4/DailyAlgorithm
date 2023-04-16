import sys
input = sys.stdin.readline

N = int(input())
board = [0] * N
for i in range(N):
    board[i] = list(map(int, input().split()))

di = [0, 1]
dj = [1, 0]

answer = 'Hing'
visited = [[0] * N for _ in range(N)]
def dfs(start, visited):
    global answer
    i, j = start[0], start[1]
    visited[i][j] = 1

    # print('i and j ', i, j)
    if (i, j) == (N-1, N-1):
        answer = 'HaruHaru'
        return 

    for n in range(2):
        jump = board[i][j]
        ni = i + di[n] * jump
        nj = j + dj[n] * jump

        if 0 <= ni < N and 0 <= nj < N:
            if not visited[ni][nj]:
                # print(visited)
                dfs([ni, nj], visited.copy())
    
dfs([0, 0], visited)          
print(answer)
            
