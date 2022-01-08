i = 1
L, P, V = map(int, input().split())
while L + P + V != 0:
    times = V // P 
    remain = min(V % P, L)
    answer = times*L + remain

    print(f'Case {i}: {answer}')
    i += 1
    L, P, V = map(int, input().split())