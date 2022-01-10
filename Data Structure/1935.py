N = int(input())
arr = input()
digit = {}
for i in range(N):
    digit[chr(65+i)] = int(input())

stack = []
for i in range(len(arr)):
    if 65 <= ord(arr[i]) <= 90:
        stack.append(digit[arr[i]])
    else:
        b = stack.pop(-1)
        a = stack.pop(-1)
        if arr[i] == '+':
            stack.append(a+b)
        elif arr[i] == '-':
            stack.append(a-b)
        elif arr[i] == '*':
            stack.append(a*b)
        elif arr[i] == '/':
            stack.append(a/b)
print(f'{stack[0]:0.2f}')