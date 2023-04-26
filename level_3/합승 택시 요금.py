import heapq

def solution(n, s, a, b, fares):
    graph = {}
    for i in range(1, n+1):
        graph[i] = {}
    for n1, n2, w in fares:
        graph[n1][n2] = w
        graph[n2][n1] = w
    
    total = float("inf")
    for i in range(1, n+1):
        total = min(total, dijkstra(graph, s, n)[i] + dijkstra(graph, i, n)[a] + dijkstra(graph, i, n)[b])
    
    # print(total)
    return total

def dijkstra(graph, start, n):
    
    dist = [float("inf")] * (n+1)
    dist[start] = 0
    q = []
    heapq.heappush(q, [dist[start], start])
    
    while q:
        cur_dist, node = heapq.heappop(q)
        
        if dist[node] < cur_dist:
            continue
        
        for new_node, new_dist in graph[node].items():
            sum_dist = cur_dist + new_dist
            if sum_dist < dist[new_node]:
                dist[new_node] = sum_dist
                heapq.heappush(q, [sum_dist, new_node])
    
    return dist
