import sys
N = int(sys.stdin.readline())

for i in range(N):
    stack = []
    arr = sys.stdin.readline()
    for i in range(len(arr)-1):
        if arr[i] == ')':
            if len(stack) !=0 and stack[-1] == '(':
                stack.pop(-1)
            else:
                stack.append(arr[i])
                break
        else:
            stack.append(arr[i])
    if len(stack) == 0:
        print('YES')
    else:
        print('NO')