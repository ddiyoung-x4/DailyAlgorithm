import heapq
import sys

N, K = map(int, sys.stdin.readline().split())

jewerly = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
bag = [int(sys.stdin.readline()) for _ in range(K)]

jewerly.sort()
bag.sort()

answer = 0
temp = []
for weight in bag:
    while jewerly and weight >= jewerly[0][0]:
        heapq.heappush(temp, -jewerly[0][1])
        heapq.heappop(jewerly)
    
    if temp:
        answer += heapq.heappop(temp)
    elif not jewerly:
        break

print(-answer)
