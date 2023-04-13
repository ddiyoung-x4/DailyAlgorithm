import sys
input = sys.stdin.readline

N = int(input())
graph = {}
for i in range(N):
    node = int(input())
    graph[node] = graph.get(node, []) + [i+1]


# cycle이 만들어지는 경우
result = []
def dfs(node, visited):
    visited.add(node)
    check[node] = 1
    
    if node in graph:
        for new_node in graph[node]:
            if new_node not in visited:
                dfs(new_node, visited.copy())
            else:
                # cycle 발생
                result.extend(list(visited))
                return

check = [0] * (N+1)
for i in range(1, N+1):
    if not check[i]:
        dfs(i, set())
result.sort()
print(len(result))
for num in result:
    print(num)
