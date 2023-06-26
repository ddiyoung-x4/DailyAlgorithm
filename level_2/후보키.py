from itertools import combinations

def solution(relation):
    answer = 0
    
    cand_key_list = []
    
    for n in range(1, len(relation[0])+1):
        for key_list in combinations(range(len(relation[0])), n):
            rel = []
            for i in range(len(relation)):
                temp = []
                for key in key_list:
                    temp.append(relation[i][key])
                rel.append(tuple(temp))
            
            # 유일성 판단
            if len(rel) == len(set(rel)):
                if n == 1:
                    cand_key_list.append(key_list)
                else:
                    # 최소성 판단
                    flag = 1
                    for cand_key in cand_key_list:
                        if set(cand_key) == set(key_list).intersection(set(cand_key)):
                            flag = 0
                            break
                    if flag:
                        cand_key_list.append(key_list)
    
    answer = len(cand_key_list)
    return answer