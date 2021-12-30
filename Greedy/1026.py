N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

sum = 0

a.sort()
for i in range(N):
    tmp = max(b)
    b.pop(b.index(tmp))
    sum += a[i]*tmp
print(sum)