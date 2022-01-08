a, b = map(int, input().split())

answer = 0
while b != a:
    if b % 10 == 1:
        b = b // 10
        answer += 1
    elif b % 2 == 0 and b != 0:
        b = b // 2
        answer += 1
    else:
        answer = -2
        break

print(answer+1)