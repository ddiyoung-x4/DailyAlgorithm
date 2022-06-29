def solution(enroll, referral, seller, amount):
    answer = []
    
    member = {'-': None}
    cost = {}
    for i, n1 in enumerate(enroll):
        member[n1] = referral[i]
        cost[n1] = 0
        
    for i, name in enumerate(seller):
        money = amount[i]*100
        money2 = int(0.1*money)
        
        while member[name] is not None and money2 > 0:
            money2 = int(0.1*money)
            money1 = money - money2
            cost[name] += money1
            
            name = member[name]
            money = money2
            
    for i, name in enumerate(enroll):
        answer.append(cost[name])
    
    return answer