import sys
input = sys.stdin.readline

seq = list(map(int, input().split()))

UP = False
DOWN = False
for i in range(7):
    if seq[i] > seq[i+1]:
        DOWN = True
    else:
        UP = True
if UP and DOWN:
    answer = 'mixed'
elif UP and not DOWN:
    answer = 'ascending'
elif not UP and DOWN:
    answer = 'descending'

print(answer)