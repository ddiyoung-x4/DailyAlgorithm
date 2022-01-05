def solution(nums):
    answer = 0
    N = len(nums)
    set_num = set(nums)
    
    if len(set_num) < N // 2:
        answer = len(set_num)
    else:
        answer = N // 2
    return answer