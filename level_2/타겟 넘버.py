# sol 1
def solution(numbers, target):
    answer = 0
    
    answer = recur_func(0, 0, numbers, target, answer)
    
    return answer

def recur_func(SUM, i, numbers, target, answer):
    if i == len(numbers) and SUM == target:
        answer += 1
    elif i < len(numbers):
        answer = recur_func(SUM+numbers[i], i+1, numbers, target, answer)
        answer = recur_func(SUM-numbers[i], i+1, numbers, target, answer)
    return answer

# sol2
# answer = 0
# def dfs(idx, numbers, target, value):
#     global answer
#     if idx == len(numbers) and target == value:
#         answer += 1
#         return
#     if idx == len(numbers):
#         return
    
#     dfs(idx+1, numbers, target, value+numbers[idx])
#     dfs(idx+1, numbers, target, value-numbers[idx])

# def solution(numbers, target):
#     global answer
#     DFS(0, numbers, target, 0)
#     return answer

