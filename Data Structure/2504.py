import sys

arr = sys.stdin.readline()
stack = []
answer = 1
for i in range(len(arr)):
    if arr[i] == '(':
        stack.append(arr[i])
    elif arr[i] == ')':
        if len(stack) and stack[-1] == '(':
            stack.pop(-1)
            stack.append(2)
        elif len(stack) and type(stack[-1]) == int:
            s = 0
            while (len(stack) and type(stack[-1]) == int):
                s += stack.pop(-1)
            if len(stack) and stack[-1] == '(':
                stack.pop(-1)
                s *= 2
            else:
                answer = 0
                break
            stack.append(s)
        else:
            answer = 0
            break
    elif arr[i] == '[':
        stack.append(arr[i])
    elif arr[i] == ']':
        if len(stack) and stack[-1] == '[':
            stack.pop(-1)
            stack.append(3)
        elif len(stack) and type(stack[-1]) == int:
            s = 0
            while (len(stack) and type(stack[-1]) == int):
                s += stack.pop(-1)
            if len(stack) and stack[-1] == '[':
                stack.pop(-1)
                s *= 3
            else:
                answer = 0
                break
            stack.append(s)
        else:
            answer = 0
            break
# print(stack)
# print(answer)
if answer == 0:
    print(answer)
else:
    s = 0
    for i in range(len(stack)):
        if type(stack[i]) != int:
            s = 0
            break
        else:
            s += stack[i]
    print(s)
        
