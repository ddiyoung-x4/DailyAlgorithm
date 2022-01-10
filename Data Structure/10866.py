import sys
N = int(sys.stdin.readline())

deque = []
for i in range(N):
    cmd = sys.stdin.readline().split()

    if cmd[0] == 'push_back':
        deque.append(int(cmd[1]))
    elif cmd[0] == 'push_front':
        l = deque
        deque = [0]
        deque[0] = int(cmd[1])
        deque.extend(l)
    elif cmd[0] == 'pop_front':
        if len(deque):
            print(deque.pop(0))
        else:
            print(-1)
    elif cmd[0] == 'pop_back':
        if len(deque):
            print(deque.pop(-1))
        else:
            print(-1)
    elif cmd[0] == 'size':
        print(len(deque))
    elif cmd[0] == 'empty':
        if len(deque):
            print(0)
        else:
            print(1)
    elif cmd[0] == 'front':
        if len(deque):
            print(deque[0])
        else:
            print(-1)
    elif cmd[0] == 'back':
        if len(deque):
            print(deque[-1])
        else:
            print(-1)