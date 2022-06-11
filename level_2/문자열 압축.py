def solution(s):
    answer = len(s)
    # 짜르는 단위
    for l in range(1, len(s)//2+1):
        # 문자열
        arr = []
        for i in range(0, len(s), l):
            arr.append(s[i:i+l])
        # print(arr)
        temp = [[arr[0], 1]]
        for i in range(1, len(arr)):
            if arr[i] == arr[i-1]:
                temp[-1][1] += 1
            else:
                temp.append([arr[i], 1])
        # print(temp)
        
        result = 0
        for i in range(len(temp)):
            if temp[i][1] == 1:
                result += len(temp[i][0])
            else:
                result += len(str(temp[i][1])) + len(temp[i][0])
        # print(result)
        answer = min(answer, result)
    return answer
