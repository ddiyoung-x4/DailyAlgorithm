str_in = list(input())
sum = 0
str_in.sort(reverse=True)

if str_in[-1] != '0': # 0 없으면 30의 배수 아님
    print(-1)
else:
    for i in str_in:
        sum += int(i)
    if sum % 3 != 0: # 모든 자릿수를 다 더한 값이 3의 배수
        print(-1)
    else:
        print(''.join(str_in))