eq = input()

digit = []
op = []
s = ''
for i, c in enumerate(eq):
    if c != '-' and c != '+':
        s += c
        if i == len(eq)-1:
            digit.append(int(s))
    else:
        op.append(c)
        digit.append(int(s))
        s = ''

total = digit[0]
sum2 = 0
for i in range(len(op)):
    if op[i] == '-':
        sum2 += sum(digit[i+1:])
        break
    if op[i] == '+':
        total += digit[i+1]
print(total - sum2)