import sys
input = sys.stdin.readline

N = int(input())
result = [0] * 3
for i in range(3):
    result[i] = list(map(int, input().split()))

temp = []
for j in range(N):
    total = result[0][j] + result[1][j] + result[2][j]
    temp.append(total)
result.append(temp)

for i in range(4):
    for j in range(N):
        result[i][j] = [result[i][j], j]
    result[i].sort(key=lambda x: x[0], reverse=True)

answer = [[0] * N for i in range(4)] 
for i in range(4):
    for j in range(N):
        if j > 0 and result[i][j][0] == result[i][j-1][0]:
            answer[i][result[i][j][1]] = answer[i][result[i][j-1][1]]
        else:
            answer[i][result[i][j][1]] = j+1

for i in range(4):
    for j in range(N):
        print(answer[i][j], end=' ')
    print()
