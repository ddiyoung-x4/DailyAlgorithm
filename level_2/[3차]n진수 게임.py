def dec2Nbit(num, N):
    ans = ''
    int2char = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}
    while num:
        remain = num % N
        if remain >= 10:
            remain = int2char[remain]
        ans += str(remain)
        num = num // N
    
    if ans == '':
        ans = '0'
    return ans[::-1]

def solution(n, t, m, p):
    answer = ''
    
    seq = ''
    for i in range(0, t*m):
        seq += dec2Nbit(i,n)
    
    for i in range(t):
        answer += seq[m*i+(p-1)]
    
    return answer