def solution(genres, plays):
    answer = []
    
    music_dict = {}
    for i, genre in enumerate(genres):
        music_dict[genre] = music_dict.get(genre, []) + [(plays[i], i)]
    order = list(music_dict.keys())
    order.sort(key=lambda x:sum([play for play, _ in music_dict[x]]), reverse=True)
    
    for genre in order:
        music_dict[genre].sort(key=lambda x:x[1], reverse=True)
        music_dict[genre].sort(key=lambda x:x[0])
        if len(music_dict[genre]) >= 2:
            _, n1 = music_dict[genre].pop()
            _, n2 = music_dict[genre].pop()
            answer.extend([n1, n2])
        else:
            _, n = music_dict[genre].pop()
            answer.append(n)
    
    return answer