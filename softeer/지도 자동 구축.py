import sys
input = sys.stdin.readline

N = int(input())

# 3^2 -> 5^2 -> 9^2 -> 
point_n = 3
for i in range(1, N):
    point_n = point_n + (point_n-1)

print(point_n**2)
