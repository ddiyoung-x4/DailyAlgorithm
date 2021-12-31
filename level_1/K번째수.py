def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        s = commands[i][0] - 1
        f = commands[i][1]
        idx = commands[i][2] - 1
        arr = sorted(array[s:f])
        answer.append(arr[idx])
    return answer