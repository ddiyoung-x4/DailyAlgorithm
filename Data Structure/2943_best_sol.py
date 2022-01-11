N = int(input())
tower = list(map(int, input().split()))
stack = []
for i in range(N):
    while stack:
        top = tower[stack[-1]]
        if top > tower[i]:
            break
        stack.pop()
        
    if stack == []:
        print(0)
    else:
        print(stack[-1]+1)
    stack.append(i)