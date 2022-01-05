import sys
def solution(N, apply):
    apply = sorted(apply, key=lambda x:x[0], reverse=False)
    cnt = 0

    m = apply[0][1]
    for i in range(N):
        if m < apply[i][1]:
            cnt += 1
        else:
            m = apply[i][1]
    return cnt
    
T = int(sys.stdin.readline())
for k in range(T):
    N = int(sys.stdin.readline())
    apply = [0] * N
    for i in range(N):
        apply[i] = (list(map(int, sys.stdin.readline().split())))

    print(N-solution(N,apply))