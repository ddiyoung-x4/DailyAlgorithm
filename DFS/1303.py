import sys
input = sys.stdin.readline

N, prob_E, prob_W, prob_S, prob_N = map(int, input().split())

# 같은 곳을 다시 오면, 이동 경로 복잡

visited = [[0] * 29 for _ in range(29)]
s_i, s_j = 14, 14
visited[s_i][s_j] = 1
# E, W, S, N
prob = [prob_E, prob_W, prob_S, prob_N]
prob = [float(x * 0.01) for x in prob]
di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

answer = 0
def dfs(i, j, visited, depth):
    global answer
    if depth == N:
        answer += visited[i][j]
        
        return
    
    for n in range(4):
        ni = i + di[n]
        nj = j + dj[n]

        if not visited[ni][nj] and prob[n] > 0:
            visited[ni][nj] = visited[i][j] * prob[n]
            dfs(ni, nj, visited.copy(), depth+1)
            visited[ni][nj] = 0
            
dfs(s_i, s_j, visited, 0)
print(answer)