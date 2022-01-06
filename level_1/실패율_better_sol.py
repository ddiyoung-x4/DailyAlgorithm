def solution(N, stages):
    fail = {}
    n_player = len(stages)
    
    for i in range(1, N+1):
        if n_player == 0:
            fail[i] = 0
        else:
            cnt = stages.count(i)
            fail[i] = (cnt/n_player)
            n_player -= cnt
    
    return sorted(fail, key=lambda x : fail[x], reverse=True)