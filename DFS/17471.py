import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

population = list(map(int, input().split()))

graph = {}
for i in range(N):
    adj_nodes = list(map(int, input().split()))[1:]
    graph[i] = [x-1 for x in adj_nodes]

result = 1000
def dfs(q, depth, limit):
    global result
    if len(q) == limit:
        sum1, cnt1 = bfs(q)
        sum2, cnt2 = bfs([x for x in range(N) if x not in q])

        if cnt1 + cnt2 == N:
            result = min(result, abs(sum1-sum2))

        return
    elif depth == N:
        return
    
    q.append(depth)
    dfs(q, depth+1, limit)
    q.pop()
    dfs(q, depth+1, limit)

def bfs(root):
    q = deque([root[0]])
    visited = [0] * N
    visited[root[0]] = 1

    SUM = 0
    while q:
        node = q.popleft()
        SUM += population[node]

        for n_node in graph[node]:
            if not visited[n_node] and n_node in root:
                q.append(n_node)
                visited[n_node] = 1
        
    return SUM, sum(visited)

for limit in range(1, N//2 +1):
    dfs([], 0, limit)

if result == 1000:
    print(-1)
else:
    print(result)