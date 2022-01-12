import itertools
import sys
arr = sys.stdin.readline()
arr = arr[:-1]

l = []
stack = []
answer = []
for i in range(len(arr)):
    if arr[i] == '(':
        stack.append([arr[i], i])
    elif arr[i] == ')':
        if len(stack) and stack[-1][0] == '(':
            _, idx = stack.pop()
            l.append([idx, i])

for i in range(1, len(l)+1):
    comb = itertools.combinations(l, i)
    for c in comb:
        add = arr
        for k, m in c:
            add = add[:k]+'_'+add[k+1:]
            add = add[:m]+'_'+add[m+1:]
        add = add.replace('_', '')
        answer.append(add)

answer = list(set(answer))
answer.sort()
for data in answer:
    print(data)