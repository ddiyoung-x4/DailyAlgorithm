from itertools import combinations
from collections import defaultdict

def solution(info, query):
    answer = []
    
    # defaultdict.append() 가 더 효율적
    # {}.get(key, []) + [value] 보다
    db = defaultdict(list)
    for line in info:
        user_info = line.split()
        score = int(user_info[-1])
        for i in range(0, 5):
            for comb in combinations(range(4), i):
                temp = user_info.copy()
                for idx in comb:
                    temp[idx] = '-'
                key = ''.join(temp[:-1])
                db[key].append(score)
                
    for key in db.keys():
        db[key].sort()
    
    for line in query:
        line = line.replace("and", "").split()
        q_key = ''.join(line[:-1])
        q_value = int(line[-1])
        
        if q_key in db:
            scores = db[q_key]
            # 이진 탐색
            start = 0
            end = len(scores)
            if len(scores) > 0:          
                start, end = 0, len(scores)     # lower bound 알고리즘 통해 인덱스 찾고,
                while start != end and start != len(scores):
                    if scores[(start + end) // 2] >= q_value:
                        end = (start + end) // 2
                    else:
                        start = (start + end) // 2 + 1
                answer.append(len(scores) - start)      # 해당 인덱스부터 끝까지의 갯수가 정답
        else:
            answer.append(0)
    return answer