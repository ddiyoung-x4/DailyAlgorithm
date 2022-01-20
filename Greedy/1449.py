import sys

N, L = map(int, sys.stdin.readline().split())
leak_point = list(map(int, sys.stdin.readline().split()))
leak_point.sort()

start = leak_point[0]
tape = 0 if len(leak_point) == 0 else 1
while leak_point:
    now = leak_point.pop(0)
    if now >= start + L:
        tape += 1
        start = now
print(tape)