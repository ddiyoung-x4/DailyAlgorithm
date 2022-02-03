import sys

N = int(sys.stdin.readline())
weight = list(map(int, sys.stdin.readline().split()))
weight.sort()

result = 0
for i in range(N):
    if result+1 >= weight[i]:
        result += weight[i]
    else:
        break
print(result+1)