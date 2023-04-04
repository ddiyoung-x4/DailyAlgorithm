def solution(number, k):
    answer = []
    max_len = len(number) - k
    for num in number:
        if not answer:
            answer.append(num)
            continue
        while answer[-1] < num and k > 0:
            answer.pop()
            k -= 1
            if not answer or k <= 0:
                break
        
        answer.append(num)
        if len(answer) == len(number) - k:
            break
        if len(answer) > max_len:
            answer = answer[:max_len]
            
    return ''.join(answer)

