N = int(input())
time = []

for i in range(N):
    a, b = map(int, input().split())
    time.append([a, b])
cnt = 0

time = sorted(time, key=lambda a: a[0])
time = sorted(time, key=lambda a: a[1])

finish_time = 0
for i, j in time:
    if i >= finish_time:
        cnt += 1
        finish_time = j

print(cnt)