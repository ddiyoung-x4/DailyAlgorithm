import sys

N, M = map(int, input().split())
mat1 = [[0] * M for _ in range(N)]
mat2 = [[0] * M for _ in range(N)]

for i in range(N):
    arr = input()
    for j in range(M):
        mat1[i][j] = int(arr[j])
for i in range(N):
    arr = input()
    for j in range(M):
        mat2[i][j] = int(arr[j])

row, col = N-3+1, M-3+1

cnt = 0
for i in range(row):
    for j in range(col):
        if mat1[i][j] != mat2[i][j]:
            cnt += 1
            for k in range(3):
                for l in range(3):
                    mat1[i+k][j+l] += 1
                    mat1[i+k][j+l] %= 2
        
        if i == row-1 and j == col-1:
            if mat1 == mat2:
                print(cnt)
                sys.exit(0)
if mat1 != mat2: 
    print(-1)
else:
    print(0)