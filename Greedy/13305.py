import sys

N = int(input())
km = list(map(int, input().split()))
money = list(map(int, input().split()))
pay = 0

m = money[0]
for i in range(N-1):
    if money[i] < m:
        m = money[i]
    pay += m*km[i]
print(pay)