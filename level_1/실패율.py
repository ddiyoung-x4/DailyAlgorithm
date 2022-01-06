def solution(N, stages):
    answer = []
    n_player = len(stages)
    fail = []
    for i in range(1, N+1):
        if n_player == 0:
            fail.append(0)
        else:
            cnt = stages.count(i)
            fail.append(cnt/n_player)
            n_player -= cnt
            
    for i in range(len(fail)):
        m = fail[0]
        idx = 0
        for j in range(len(fail)):
            if m < fail[j]:
                m = fail[j]
                idx = j
        answer.append(idx+1)
        fail[idx] = -1
    return answer