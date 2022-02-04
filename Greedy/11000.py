import sys
import heapq

N = int(sys.stdin.readline())
course = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

course = sorted(course, key=lambda x:x[1])
course = sorted(course, key=lambda x:x[0])

q = []
for i, j in course:
    if len(q) and i >= q[0]:
        heapq.heappop(q)
    heapq.heappush(q, j)
    
print(len(q))