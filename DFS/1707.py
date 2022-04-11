import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(node):
    global answer

    for next in graph[node]:
        if set_cls[next] == -1:
            # 아직 방문x node
            set_cls[next] = (set_cls[node] + 1) % 2
            dfs(next)
        else:
            # 이미 방문o node
            if set_cls[node] == set_cls[next]:
                # 인접한데 같은 group
                answer = False
            


K = int(input())
for k in range(K):
    V, E = map(int, input().split())
    set_cls = [-1] * (V+1)
    graph = [[] for _ in range(V+1)]
    for _ in range(E):
        n1, n2 = map(int, input().split())
        graph[n1].append(n2)
        graph[n2].append(n1)
    answer = True
    for i in range(1, V+1):
        dfs(i)
    if answer:
        print('YES')
    else:
        print('NO')