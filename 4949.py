import sys
input = sys.stdin.readline

while True:
    sentence = input().rstrip()

    if sentence == ".":
            break

    answer = 'yes'
    stack = []
    for ch in sentence:
        if ch == '[' or ch == '(':
            stack.append(ch)
        elif ch == ']':
            if len(stack) == 0:
                answer = 'no'
                break
            else:
                before_ch = stack.pop()
                if before_ch != '[':
                    answer = 'no'
                    break
        elif ch == ')':
            if len(stack) == 0:
                answer = 'no'
                break
            else:
                before_ch = stack.pop()
                if before_ch != '(':
                    answer = 'no'
                    break
    if len(stack) > 0:
        answer = 'no'
    print(answer)
