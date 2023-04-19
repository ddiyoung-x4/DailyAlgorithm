from collections import deque

def solution(progresses, speeds):
    answer = []
    progresses = deque(progresses)
    speeds = deque(speeds)
    
    while len(progresses) > 0:
        for i in range(len(progresses)):
            progresses[i] += speeds[i]

        cnt = 0
        while len(progresses) > 0 and progresses[0] >= 100:
            cnt += 1
            progresses.popleft()
            speeds.popleft()
        if cnt > 0:
            answer.append(cnt)
    
    return answer