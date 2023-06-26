def check_correct(sen):
    stack = []
    
    for s in sen:
        if s == '(':
            stack.append('(')
        elif s == ')':
            if not stack:
                stack.append('(')
            else:
                if stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append('(')
            
    if len(stack) != 0:
        return False
    else:
        return True

def recur(sen):
    
    # 1
    if sen == '':
        return ''
    
    # 2 u, v 분리
    left_p = 0
    right_p = 0
    if sen[0] == '(':
        left_p += 1
    else:
        right_p += 1
    
    i = 1
    while left_p != right_p:
        if sen[i] == '(':
            left_p += 1
        else:
            right_p += 1
        i += 1
    u, v = sen[:i], sen[i:]
    
    # 3
    if check_correct(u):
        return u + recur(v)
    else:
        u_temp = ''
        if len(u) > 2:
            for d in u[1:-1]:
                if d == '(':
                    u_temp += ')'
                else:
                    u_temp += '('
                    
        u_temp = '(' + recur(v) + ')' + u_temp
        
        return u_temp

def solution(p):
    answer = ''
        
    answer = recur(p)
    
    return answer