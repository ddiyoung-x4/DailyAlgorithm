def solution(prices):
    answer = [0] * len(prices)
    stack = []
    
    for i, price in enumerate(prices):
        while stack and price < prices[stack[-1]]:
            idx = stack.pop()
            answer[idx] = i - idx
        
        stack.append(i)
    
    while stack:
        idx = stack.pop()
        answer[idx] = len(prices) - idx - 1
    return answer