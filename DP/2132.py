N = int(input())

DP = [0] * (31)
DP[2] = 3
# DP 2 = 0
# DP 4 = DP 2 * 3y + 1
# DP 6 = DP 4 * 3y + 1

if N % 2 == 1: # 짝수만 가능
    print(0)
else:
    for n in range(4, N+1, 2):
        DP[n] = DP[n-2]*3 + 2*sum(DP[:n-2]) + 2
        # 0 -> 1 -> 3y + 1 -> 3^2y + 3y + 1
        # 2    4    6         8
    print(DP[N])