import sys
input = sys.stdin.readline

N, M = map(int, input().split())

edge = [list(map(int, input().split())) for _ in range(M)]
# A가 B를 신뢰한다
graph={}

for i in range(1, N+1):
    l = list()
    for j in range(M):
        if i == edge[j][1]:
            l.append(edge[j][0])
    graph[i] = l

global_set = set()
for i in range(1, N+1):
    global_set.add(i)

while global_set:
    def bfs(root):
        del_set = set()
        queue = list()
        visit = [0] * (N+1)
        queue.append(root)

        while queue:
            a = queue[0]
            del_set.add(a)
            del queue[0]

            for node in graph[a]:
                if visit[node] == 0 and node in global_set:
                    visit[node] = 1
                    queue.append(node)
        return del_set

    # print(global_set)
    MAX = -1
    for i in global_set:
        temp = len(bfs(i))
        if MAX < temp:
            MAX = temp
            idx = i

    for del_node in bfs(idx):
        # print(f'what to del: {del_node}')
        global_set.remove(del_node)

    print(idx, end=' ')