import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

N, M, R = map(int, input().split())
graph = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


visited = [0] * (N+1)
depth = 1
def dfs(R):
    global depth
    visited[R] = depth
    graph[R].sort()
    
    for node in graph[R]:
        if not visited[node]:
            depth += 1
            dfs(node)

dfs(R)
for i in range(1, N+1):
    print(visited[i])