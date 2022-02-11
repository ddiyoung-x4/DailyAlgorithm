import sys

N, K = map(int, sys.stdin.readline().split())
seq = list(map(int, sys.stdin.readline().split()))

plug = []
cnt = 0
for i in range(len(seq)):
    if seq[i] not in plug and len(plug) < N:
        plug.append(seq[i])
    elif seq[i] not in plug and len(plug) == N:
        idx = [K] * N
        for j in range(N):
            for k in range(i+1, len(seq)):
                if seq[k] == plug[j]:
                    idx[j] = k
                    break
        print('idx', idx)
        tmp = max(idx)
        plug[idx.index(tmp)] = seq[i]
        cnt += 1
    print(plug)
print(cnt)
