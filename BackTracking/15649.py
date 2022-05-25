import sys
input = sys.stdin.readline

N, M = map(int, input().split())

visited = [0] * (N+1)

answer = []

def dfs():
    if len(answer) == M:
        for data in answer:
            print(data, end=' ')
        print()
        return
    
    for i in range(1, N+1):
        if i not in answer:
            answer.append(i)
            dfs()
            answer.pop()
dfs()