def solution(citations):
    answer = 0
    
    citations.sort(reverse=True)
    for i, n_cite in enumerate(citations):
        if n_cite <= i:
            return i
        
    return len(citations)