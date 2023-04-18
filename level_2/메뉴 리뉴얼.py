from itertools import combinations
from collections import defaultdict

def solution(orders, course):
    answer = []
        
    db, max_cnt = make_db(orders, course)
    for key in db.keys():
        if db[key] >= 2:
            for i in range(len(course)):
                if len(key) == course[i] and db[key] == max_cnt[i]:
                    answer.append(key)
    answer.sort()
    return answer

def make_db(orders, course):
    
    db = defaultdict(int)
    max_cnt = [0] * len(course)
    
    for i, size in enumerate(course):
        for order in orders:
            order = list(order)
            order.sort()
            order = ''.join(order)


            for comb in combinations(order, size):
                temp = ''.join(comb)
                db[temp] += 1
                
                max_cnt[i] = max(max_cnt[i], db[temp])
                
    return db, max_cnt
