import sys

cnt = 0
d = {}
for line in sys.stdin:
    if line == '\n':
        break
    line = line[:-1]
    if line in d:
       a = d[line]
       d[line] = a+1
    else:
        d[line] = 1
    cnt += 1

arr = sorted(d, key=lambda x: x)
for i in range(len(arr)):
    percent = d[arr[i]]/cnt*100
    print(arr[i], f'{percent:.4f}')