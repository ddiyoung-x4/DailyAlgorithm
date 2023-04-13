from collections import deque

def solution(n, costs):
    answer = 0
    
    graph = [[0] * n for _ in range(n)]
    for x, y, d in costs:
        graph[x][y] = d
        graph[y][x] = d
    
    answer = bfs([0, 0], graph)
    
    return answer


def find_adj_node(node, graph):
    n = len(graph)
    adj_nodes = []
    for i in range(n):
        if graph[node][i] > 0:
            adj_nodes.append([i, graph[node][i]])
    
    adj_nodes.sort(key=lambda x:x[1])
    return adj_nodes

# Prim's Algorithm
def bfs(root, graph):
    n = len(graph)
    q = deque([root])
    visited = [0] * n
    
    answer = 0
    cnt = 0
    while q:
        print(q)
        q = deque(sorted(q, key=lambda x:x[1]))
        node, d = q.popleft()
        if visited[node]:
            continue
        answer += d
        cnt += 1
        visited[node] = 1
        
        for adj_node, dist in find_adj_node(node, graph):
            if not visited[adj_node]:
                q.append([adj_node, dist])
                
    return answer
        