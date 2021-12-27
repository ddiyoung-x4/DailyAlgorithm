people = int(input())
t = list(map(int, input().split()))

min_t = 0
t.sort()
for i in range(len(t)):
    for j in range(i+1):
        min_t += t[j]

print(min_t)