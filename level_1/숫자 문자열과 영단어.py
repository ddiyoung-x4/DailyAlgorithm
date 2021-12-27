import re

def solution(s):
    answer = 0
    
    eng_num = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    for i in range(len(eng_num)):
        if eng_num[i] in s:
            s = re.sub(eng_num[i], str(i), s)
    
    return int(s)