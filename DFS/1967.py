import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(node):
    for next_node, weight in graph[node]:
        if dist[next_node] == -1:
            dist[next_node] = dist[node] + weight
            dfs(next_node)

N = int(input())
graph = [[] for _ in range(N+1)]
for _ in range(N-1):
    n1, n2, dist = map(int, input().split())
    graph[n1].append([n2, dist])
    graph[n2].append([n1, dist])

dist = [-1] * (N+1)
dist[1] = 0
dfs(1)
n1 = dist.index(max(dist))
dist = [-1] * (N+1)
dist[n1] = 0
dfs(n1)
print(max(dist))