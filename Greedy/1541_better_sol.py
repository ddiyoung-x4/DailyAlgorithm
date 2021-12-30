eq = input().split('-')
print(eq)

total = 0
for data in eq[0].split('+'):
    total += int(data)
for i in range(1, len(eq)):
    for data in eq[i].split('+'):
        total -= int(data)

print(total)