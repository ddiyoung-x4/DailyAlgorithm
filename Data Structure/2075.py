N = int(input())
table = []
for i in range(N):
    table.append(list(map(int, input().split())))

stack = []
idx = [N-1] * N
for _ in range(N):
    tmp = 0
    id = 0
    for i in range(N):
        a = table[idx[i]][i]
        if a > tmp:
            tmp = a
            id = i
    
    if _ == N-1:
        print(table[idx[id]][id])
    idx[id] -= 1