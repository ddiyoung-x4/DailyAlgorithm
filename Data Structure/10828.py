import sys
N = int(sys.stdin.readline())

stack = []
for i in range(N):
    cmd = sys.stdin.readline().split()

    if cmd[0] == 'push':
        stack.append(int(cmd[1]))
    elif cmd[0] == 'top':
        if len(stack):
            print(stack[-1])
        else:
            print(-1)
    elif cmd[0] == 'size':
        print(len(stack))
    elif cmd[0] == 'empty':
        if len(stack):
            print(0)
        else:
            print(1)
    elif cmd[0] == 'pop':
        if len(stack):
            print(stack.pop(-1))
        else:
            print(-1)