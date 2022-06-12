import math

def change_k(n, k):
    temp = ''
    while n != 0:
        temp += str(n%k)
        n = n // k
    return temp[::-1]

def is_prime(num):
    if num == 1:
        return False
    
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True
       

def solution(n, k):
    answer = 0
    temp = change_k(n, k)
    
    arr = temp.split('0')
    for num in arr:
        if num and is_prime(int(num)):
            # print(num)
            answer += 1

    return answer