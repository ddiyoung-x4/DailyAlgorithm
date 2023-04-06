from collections import deque

N, M = map(int, input().split())

board = [0] * N
chicken = []
house = []
for i in range(N):
    board[i] = list(map(int, input().split()))
    for j in range(N):
        if board[i][j] == 1:
            house.append([i, j])
        elif board[i][j] == 2:
            chicken.append([i, j])

# itertools 없이 dfs combinations 구현
MinValue = 2 * N * N * M
def dfs(q, depth):
    global MinValue
    if len(q) == M:
        print(q)
        # 치킨 집 M 개 선택 후
        # print(q)
        dsum = 0
        for i1, j1 in house:
            MIN = 2 * N + 1
            for i2, j2 in q:
                MIN = min(abs(i1-i2)+abs(j1-j2), MIN)
            dsum += MIN
        MinValue = min(dsum, MinValue)
        return
    elif depth == len(chicken):
        return
    
    q.append(chicken[depth])
    dfs(q, depth+1)
    q.pop()
    dfs(q, depth+1)

dfs(deque(), 0)
print(MinValue)