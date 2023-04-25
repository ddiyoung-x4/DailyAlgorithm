import math
from itertools import combinations

def check(num_bin, prev_parent):
    # 중앙값(자손) 기준으로 재귀적으로 확인
    mid = len(num_bin) // 2
    if num_bin:
        son = (num_bin[mid] == '1')
    else:
        return True
    
    # 내가 존재하면 부모가 존재해야함.
    if son and not prev_parent:
        return False
    else:
        return check(num_bin[mid + 1:], son) and check(num_bin[:mid], son)

def solution(numbers):
    answer = []
    
    for num in numbers:
        # 2진수 변환
        num_bin = bin(num)[2:]
        # 2^n - 1꼴의 자릿수를 가져야함.
        digit = 2 ** (int(math.log2(len(num_bin))) + 1) - 1
        num_bin = "0" * (digit - len(num_bin)) + num_bin
        
        if num_bin[len(num_bin) // 2] == '1'and check(num_bin, True):
            answer.append(1)
        else:
            answer.append(0)

    return answer

