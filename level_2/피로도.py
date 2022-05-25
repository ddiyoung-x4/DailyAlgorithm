result = 0

def dfs(remain_dungeons, k, res, dungeons):
        global result 
        
        result = max(res, result)
        
        for idx, (min_stress, used_stress) in enumerate(dungeons):
            if idx in remain_dungeons:
                # print('idx: ', idx, ', k: ', k, ', res: ', res)
                remain_dungeons.remove(idx)
                if min_stress <= k:
                    dfs(remain_dungeons, k - used_stress, res+1, dungeons)
                remain_dungeons.append(idx)

def solution(k, dungeons):
    dg_list = [d for d in range(len(dungeons))]
    
    dfs(dg_list, k, 0, dungeons)
    
    return result