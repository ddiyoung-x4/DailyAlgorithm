import sys
input = sys.stdin.readline

board = [[0] * 5 for _ in range(5)]
for i in range(5):
    board[i] = list(map(int, input().split()))


di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
answer = []
def dfs(seq, i, j, depth):
    if depth == 5:
        if seq not in answer:
            answer.append(seq)
        return

    for n in range(4):
        ni = i + di[n]
        nj = j + dj[n]

        if 0 <= ni < 5 and 0 <= nj < 5:
            seq += str(board[ni][nj])
            dfs(seq, ni, nj, depth+1)
            seq = seq[:-1]

for i in range(5):
    for j in range(5):
        dfs(str(board[i][j]), i, j, 0)
print(len(answer))