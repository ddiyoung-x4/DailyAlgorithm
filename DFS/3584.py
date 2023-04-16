import sys
input = sys.stdin.readline

T = int(input())

def find_root(node):
    parent = node
    path = [node]
    while parent != 0:
        parent = graph[node]['parent']
        node = parent
        path.append(parent)

    return path
for _ in range(T):
    N = int(input())
    graph = {}
    for i in range(N-1):
        a, b = map(int, input().split())
        graph[a] = graph.get(a, {'parent': 0, 'child': []})
        graph[a]['child'].append(b)
        graph[b] = graph.get(b, {'parent': 0, 'child': []})
        graph[b]['parent'] = a
    
    node1, node2 = map(int, input().split())
    
    path1 = find_root(node1)
    path2 = find_root(node2)
    
    for num in path1:
        if num in path2:
            print(num)
            break




