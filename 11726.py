import math

n = int(input())

sum = 0
for r in range(n//2+1):
    # n은 그대로, r은 1씩 증가
    N = n-r
    numerator = math.factorial(N)
    denomiator = math.factorial(N-r) * math.factorial(r)
    nCr = numerator//denomiator

    sum += nCr
print(sum%10007)

# n = int(input())

# DP = [0] * (n+1)
# DP[1] = 1
# if n >= 2:
#     DP[2] = 2
# for i in range(3, n+1):
#     DP[i] = DP[i-1] + DP[i-2]
# print(DP[n]%10007)