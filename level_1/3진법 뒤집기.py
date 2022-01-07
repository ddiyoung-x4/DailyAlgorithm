def solution(n):
    answer = 0
    s = ''
    while n > 0:
        remain = n % 3
        n = n // 3
        s += str(remain)
    
    for i in range(len(s)):
        answer += int(s[i])*3**(len(s)-1-i)
    return answer