from collections import deque

def bfs(root, n, graph):
    q = deque([root])
    visited = [0]*(n+1)
    length = 1
    while q: 
        node = q.popleft()
        visited[node] = 1
        for next_node in graph[node]:
            if not visited[next_node]:
                q.append(next_node)
                length += 1
    return length
        

def solution(n, wires):
    graph = {}
    
    for i, j in wires:
        if i not in graph:
            graph[i] = [j]
        if j not in graph:
            graph[j] = [i]
        if j not in graph[i]:
            graph[i].append(j)
        if i not in graph[j]:
            graph[j].append(i)
    MIN = 100
    for i, j in wires:
        graph[i].remove(j)
        graph[j].remove(i)
        tmp = abs(bfs(i, n, graph)-bfs(j, n, graph))
        graph[i].append(j)
        graph[j].append(i)
        if MIN > tmp:
            MIN = tmp
    return MIN