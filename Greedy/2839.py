def solution(N):
    cnt = 0

    # greedy algorithm
    # 현재 최선의 선택 -> 일단 제일 높은 수부터 선택하고 안되면 낮은 수
    while N >= 0:
        if N % 5 == 0:
            cnt += N // 5
            N = 0
            break
        N -= 3
        cnt += 1
    if N != 0:
        cnt = -1

    return cnt

data = int(input())
print(solution(data))