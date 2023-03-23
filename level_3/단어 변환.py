def solution(begin, target, words):
    answer = 0
    if target not in words:
        return 0
    
    n = len(words)
    # words 단어 간의 dist matrix 만들기
    dist = [[0] * n for i in range(n)]
    for i in range(0, n-1):
        for j in range(1, n):
            word1 = words[i]
            word2 = words[j]
            cnt = 0
            for k in range(len(word1)):
                if word1[k] != word2[k]:
                    cnt += 1
            dist[i][j] = cnt
            dist[j][i] = cnt


    q = []
    visited = [0] * n
    
    # begin과 words 간의 dist=1 단어 찾기
    for i in range(n):
        cnt = 0
        for j in range(len(begin)):
            if begin[j] != words[i][j]:
                cnt += 1
        if cnt == 1:
            q.append(i)
            visited[i] = 1
    
    # bfs로 target 단어까지 몇번 변환하는지 탐색
    while q:
        node = q.pop(0)
        
        print('node', node)
        for i in range(n):
            if dist[node][i] == 1 and not visited[i]:
                visited[i] = visited[node] + 1
                q.append(i)
    answer = visited[words.index(target)]
    
    return answer