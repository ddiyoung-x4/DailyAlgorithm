N, K = map(int, input().split())
A = []
for i in range(N):
    A.insert(0, int(input()))

cnt = 0
for i in range(len(A)):
    if K // A[i] > 0:
        cnt += K // A[i]
        K = K % A[i]
print(cnt)    

