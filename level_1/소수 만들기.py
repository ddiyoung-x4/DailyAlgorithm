import itertools
import math

def is_prime(num):
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    return True
def solution(nums):
    cnt = 0
    result = list(itertools.combinations(nums,3))
    for i in range(len(result)):
        num = sum(result[i])
        if is_prime(num):
            cnt += 1

    return cnt