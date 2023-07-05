from collections import deque

def solution(cacheSize, cities):
    answer = 0
    cache = deque()
    for i, city in enumerate(cities):
        city = city.lower()
        if city not in cache:
            if len(cache) >= cacheSize and cacheSize != 0:
                cache.popleft()
            answer += 5
        else:
            cache.remove(city)
            answer += 1
        if cacheSize != 0:
            cache.append(city)
    
    return answer