import math

def solution(w,h):
    if w == h:
        return w*h - w
    elif w == 1 or h == 1:
        return 0
    
    answer = w*h
    cnt = 0
    
    gcd = math.gcd(w, h)
    w = w // gcd
    h = h // gcd
    delta = h/w
    for x in range(1, w+1):
        y0 = delta*(x-1)
        y1 = delta*x
        if y1 - int(y1) == 0:
            y1 = int(y1)
        else:
            y1 = int(y1)+1
        
        cnt += y1-int(y0)
        
    return answer - gcd*cnt

def another_solution(w, h):
    gcd = math.gcd(w, h)
    w2 = w // gcd
    h2 = h // gcd
    return w*h - (w2+h2-1)*gcd