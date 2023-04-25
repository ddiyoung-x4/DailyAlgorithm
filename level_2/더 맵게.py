import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    
    cnt = 0
    while scoville:
        if len(scoville) >= 2 and  scoville[0] < K:
            a = heapq.heappop(scoville)
            b = heapq.heappop(scoville)
            heapq.heappush(scoville, a + b * 2)
            cnt += 1
        else:
            break
    
    if scoville[0] < K:
        cnt = -1
        
    return cnt