from collections import deque

def solution(priorities, location):
    answer = 0
    
    priorities = [[priorities[x], x] for x in range(len(priorities))]
    priorities = deque(priorities)
    
    prior = 0
    while priorities:
        if priorities[0][0] < max([x for x, _ in priorities]):
            a, b = priorities.popleft()
            priorities.append([a, b])
        else:
            _, idx = priorities.popleft()
            prior += 1
            if idx == location:
                answer = prior
                break
    
    return answer