from collections import deque 
def solution(queue1, queue2):
    queue1, queue2 = deque(queue1), deque(queue2)
    
    cnt = 0
    MAX_cnt = len(queue1)*4
    if (sum(queue1) + sum(queue2)) % 2 == 1:
        return -1
    
    q1_sum = sum(queue1)
    q2_sum = sum(queue2)
    while q1_sum != q2_sum:
        if len(queue1) == 0 or len(queue2) == 0:
            return -1
        if cnt > MAX_cnt:
            cnt = -1
            break
            
        if q1_sum < q2_sum:
            num = queue2.popleft()
            queue1.append(num)
            q1_sum += num
            q2_sum -= num
        elif q1_sum > q2_sum:
            num = queue1.popleft()
            queue2.append(num)
            q2_sum += num
            q1_sum -= num
            
        cnt += 1
        
    # print(cnt)
    return cnt

# 14 16 -> 30 / 2 = 15
# 18 12
# 15 15

# 6 14 -> 20 / 2 = 10
# 7 13
# 17 3
# 16 4
# 14 6
# 13 7
# 11 9
# 10 10

# 2 6 -> 8 / 2 = 4

# 5 