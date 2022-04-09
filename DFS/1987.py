import sys

# 좌, 하, 우, 상
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def DFS(x, y, ans):
    global answer

    answer = max(ans, answer)

    # 좌우상화 다 확인한다
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # index 벗어나지 않는지 체크하고, 새로운 칸이 중복되는 알파벳인지 체크한다
        if ((0 <= nx < R) and (0 <= ny < C)) and not alpha[ord(board[nx][ny]) - ord('A')]:
            alpha[ord(board[nx][ny]) - ord('A')] = 1
            DFS(nx, ny, ans+1)
            alpha[ord(board[nx][ny]) - ord('A')] = 0

R, C = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().strip()) for _ in range(R)]

alpha = [0] * 26
alpha[ord(board[0][0]) - ord('A')] = 1
answer = 1
DFS(0, 0, answer)
print(answer)