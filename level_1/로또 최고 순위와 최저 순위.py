def solution(lottos, win_nums):
    answer = []
    cnt = 0
    zero = 0
    for i, data in enumerate(lottos):
        if data in win_nums:
            cnt += 1
        if data == 0:
            zero += 1
    answer = [7-(cnt+zero) if (cnt+zero) != 0 else 6, 7-cnt if cnt >= 2 else 6]
    return answer