N, K = map(int, input().split())
arr = [i for i in range(1, N+1)]
answer = []
idx = 0

for i in range(N):
    idx += K-1
    idx = idx % len(arr)
    answer.append(arr.pop(idx))

print('<', end='')
for i in range(len(answer)-1):
    print(answer[i], end=', ')
print(f'{answer[-1]}>')