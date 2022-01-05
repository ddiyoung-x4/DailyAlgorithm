N = int(input())
rope = []
maximum = 0

for i in range(N):
    weight = int(input())
    rope.append(weight)

rope.sort(reverse=True)    
for i in range(len(rope)):
    rope[i] = rope[i] * (i+1)

print(max(rope))