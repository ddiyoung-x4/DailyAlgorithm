import sys
from collections import deque
input = sys.stdin.readline

def bfs(graph, root):
    queue = deque([root])
    visited = [0] * (N+1)
    visited[root] = 1
    cnt = 1

    while queue:
        node = queue.popleft()

        for next in graph[node]:
            if not visited[next]:
                visited[next] = 1
                queue.append(next)
                cnt += 1
    return cnt


N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    n1, n2 = map(int, input().split())
    graph[n2].append(n1)

MAX = 0
ans_list = []
for i in range(1, N+1):
    ans = bfs(graph, i)
    if ans >= MAX:
        MAX = ans
        ans_list.append([i, ans])
for idx, ans in ans_list:
    if ans == MAX:
        print(idx, end=' ')