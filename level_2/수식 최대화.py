import re
from itertools import permutations

def calculate(op, num1, num2):
    if op == '+':
        return num1+num2
    elif op == '-':
        return num1-num2
    elif op == '*':
        return num1*num2

def infix2postfix(exp, prior_dict):
    res = []
    stack = []
    
    for e in exp:
        if e not in ['+','-','*']:
            res.append(e)
        else:
            if not stack:
                stack.append(e)
            else:
                while len(stack) > 0:
                    if prior_dict[stack[-1]] >= prior_dict[e]:
                        res.append(stack.pop())
                    else:
                        break
                stack.append(e)
    
    while stack:
        res.append(stack.pop())
    
    return res

def compute_postfix(exp):
    
    stack = []
    for e in exp:
        if e not in ['+','-','*']:
            stack.append(e)
        else:
            b = stack.pop()
            a = stack.pop()
            res = calculate(e, a, b)
            stack.append(res)
    return stack.pop()

def solution(expression):
    answer = 0
    
    num_stack=[]
    op_stack=[]
    
    operators = []
    for e in expression:
        if e in ['+', '-', '*']:
            operators.append(e)
    numbers = re.split('[\+\-\*]', expression)
          
    exp = []
    for i, op in enumerate(operators):
        exp.append(int(numbers[i]))
        exp.append(op)
    exp.append(int(numbers[-1]))
    
    for prior in permutations(['+','-','*']):
        temp_dict={}
        for i, op in enumerate(prior):
            temp_dict[op] = 3-i
        
        ans = compute_postfix(infix2postfix(exp,temp_dict))
        answer = max(answer, abs(ans))
    return answer