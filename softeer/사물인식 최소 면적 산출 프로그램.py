import sys
input = sys.stdin.readline

N, K = map(int, input().split())
color = [[] for i in range(K+1)]

for i in range(N):
    x, y, k = map(int, input().split())
    color[k].append([x, y])

answer = (2001) ** 2
def dfs(num, minX, minY, maxX, maxY, color):
    global answer
    if num > K:
        now = abs(maxX-minX) * abs(maxY-minY)
        if answer > now:
            answer = now
        return

    if color[num]:
        for nx, ny in color[num]:
            NminX = min(minX, nx)
            NmaxX = max(maxX, nx)
            NminY = min(minY, ny)
            NmaxY = max(maxY, ny)

            dx = NmaxX - NminX
            dy = NmaxY - NminY
            temp = dx * dy
            if answer > temp:
                dfs(num+1, NminX, NminY, NmaxX, NmaxY, color)
            
for x, y in color[1]:
    dfs(2, x, y, x, y, color)
print(answer)