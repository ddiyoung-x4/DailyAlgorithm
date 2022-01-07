N = int(input())
num = [''] * N
weight = {}
char2digit = {}
start = 9

for i in range(N):
    num[i] = input()

for i in range(N):
    length = len(num[i])
    for j in range(len(num[i])):
        ch = num[i][j]
        if ch in weight:
            org = weight[ch]
            org += 10**(length-j-1)
            weight[ch] = org
        else:
            weight[ch] = 10**(length-j-1)

char2digit = sorted(weight, key=lambda x: weight[x], reverse=True)

sum = 0
for key in char2digit:
    sum += weight[key]*start
    start -= 1
print(sum)