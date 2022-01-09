N = int(input())
a = [0] * N
for i in range(N):
    a[i] = int(input())

a.sort(reverse=True)

i = 0
total = 0
while a:
    if a[i] > 0:
        num1 = a.pop(0)
        if len(a) == 0:
            total += num1
        elif a[i] > 1:
            num2 = a.pop(0)
            total += num1 * num2
        elif a[i] == 1:
            num2 = a.pop(0)
            total += num1+num2
        else:
            total += num1
    elif a[i] == 0:
        num1 = a.pop(0)
        if len(a) % 2 != 0:
            num2 = a.pop(0)
    else:
        if len(a) % 2 == 0:
            num1 = a.pop(0)
            num2 = a.pop(0)
            total += (num1*num2)
        else:
            num1 = a.pop(0)
            total += num1
print(total)