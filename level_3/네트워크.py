def solution(n, computers):
    answer = 0
    
    visited = [0] * n
    
    for i in range(n):
        if not visited[i]:
            answer += 1
        
        q = [i]

        while q:
            node = q.pop(0)

            if not visited[node]:
                visited[node] = 1
                for i in range(n):
                    if computers[node][i] and not visited[i]:
                        q.append(i)
    return answer
