def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        a = bin(arr1[i])[2:]
        b = bin(arr2[i])[2:]
        # tmp = ''
        # for j in range(n-len(a)):
        #     tmp += '0'
        # a = tmp + a
        a = a.rjust(n, '0')
        # tmp = ''
        # for j in range(n-len(b)):
        #     tmp += '0'
        # b = tmp + b
        b = b.rjust(n, '0')

        tmp = ''
        for j in range(n):
            if a[j] == '1' or b[j] == '1':
                tmp += '#'
            else:
                tmp += ' '
                
        answer.append(tmp)
    return answer