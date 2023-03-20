import math
import itertools

def solution(numbers):
    answer = 0
    
    num_list = list(numbers)
    for i in range(1, len(num_list)+1):
        new_one = itertools.permutations(num_list, i)
        new_list = []
        for j in new_one:
            new_list.append(int("".join(j)))
        new_set = set(new_list)
        for num in new_set:
            if is_prime(num) and len(str(num)) == i:
                answer += 1
    return answer

def is_prime(num):
    if num < 2:
        return False
    
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            return False
    
    return True
    