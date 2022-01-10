import heapq
import sys
N = int(sys.stdin.readline())

p_q = []
heapq.heapify(p_q)

for i in range(N):
    l = list(map(int, sys.stdin.readline().split()))
    for j in range(len(l)):
        heapq.heappush(p_q, l[j])
        if len(p_q) > N:
            heapq.heappop(p_q)

print(p_q[0])
