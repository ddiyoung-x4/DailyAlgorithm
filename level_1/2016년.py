def solution(a, b):
    answer = ''
    mon = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30]
    date = ['THU','FRI','SAT','SUN','MON','TUE','WED']
    sum = 0
    for i in range(a):
        sum += mon[i]
    b += sum
    answer = date[b%7]
    return answer