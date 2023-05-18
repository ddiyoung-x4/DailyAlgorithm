def solution(today, terms, privacies):
    answer = []
    
    priv_dict = {}
    for term in terms:
        priv, num = term.split()
        priv_dict[priv] = int(num)
    
    for idx, line in enumerate(privacies):
        date, term = line.split()
        yy = int(date[0:4]) * 12 * 28
        mm = int(date[5:7]) * 28
        dd = int(date[8:])
        
        date = yy + mm + dd - 1 + priv_dict[term] * 28
        n_date = int(today[0:4]) * 12 * 28 + int(today[5:7]) * 28 + int(today[8:])
        
        if n_date > date:
            answer.append(idx+1)
    
    return answer