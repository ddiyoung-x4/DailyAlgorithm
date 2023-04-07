from collections import deque

N, Q = map(int, input().split())

board = [0] * 2**N
for i in range(2**N):
    board[i] = list(map(int, input().split()))

L_list = list(map(int, input().split()))


# 시계 방향 90도 회전
def rotate90(org):
    reversed_ = org[::-1]
    rotated = list(zip(*reversed_))
    for i in range(len(rotated)):
        rotated[i] = list(rotated[i])
    return rotated


# a = [[1,2,3,4],
#      [5,6,7,8],
#      [9,10,11,12],
#      [13,14,15,16]]

# t = [[(8 * i + j) for j in range(1, 9)] for i in range(8)]


dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

# 격자 생성
for L in L_list:
    if L > 0:
        for i in range(2**N // 2**L):
            for j in range(2**N // 2**L):
                temp = []
                for k in range(2**L):
                    temp.append(board[i * 2**L + k][j * 2**L: j * 2**L + 2**L])
                temp = rotate90(temp)
                for k in range(2**L):
                    board[i * 2**L + k][j * 2**L: j * 2**L + 2**L] = temp[k]
    
    # 얼음 양 1 감소, 상하좌우 얼음 칸 3개 미만 경우
    temp = []
    for i in range(2**N):
        for j in range(2 ** N):
            if board[i][j] > 0:
                check_cnt = 0
                for k in range(4):
                    ni = i + dy[k]
                    nj = j + dx[k]

                    if 0 <= ni < 2**N and 0 <= nj < 2**N:
                        if board[ni][nj] > 0:
                            check_cnt += 1
                if check_cnt < 3:
                    temp.append([i, j])
    # 얼음 감소 일괄처리
    for i, j in temp:
        board[i][j] -= 1

answer2 = 0
def bfs(root):
    global answer2
    q = deque([root])
    cnt = 1

    while q:
        i, j = q.popleft()

        for k in range(4):
            ni = i + dy[k]
            nj = j + dx[k]

            if 0 <= ni < 2**N and 0 <= nj < 2**N:
                if not visited[ni][nj] and board[ni][nj] > 0:
                    visited[ni][nj] = 1
                    cnt += 1
                    q.append([ni, nj])
    answer2 = max(answer2, cnt)



# 가장 큰 덩어리 찾기
visited = [[0] * (2**N) for _ in range(2**N)]
for i in range(2**N):
    for j in range(2**N):
        if board[i][j] > 0:
            visited[i][j] = 1
            bfs([i, j])

answer1 = 0
for i in range(2**N):
    for j in range(2**N):
        answer1 += board[i][j]
print(answer1)
print(answer2)