import heapq

N = int(input())
trump = [0] * N
for i in range(N):
    trump[i] = int(input())

heapq.heapify(trump)
total = 0
while len(trump) > 1:
    tmp1 = heapq.heappop(trump)
    tmp2 = heapq.heappop(trump)
    total += tmp1+tmp2
    heapq.heappush(trump, tmp1+tmp2)

print(total)
