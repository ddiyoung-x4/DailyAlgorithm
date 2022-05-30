def solution(line):
    answer = []
    star = []
    for i in range(len(line)):
        for j in range(i+1, len(line)):
            a, b, e = line[i]
            c, d, f = line[j]
            
            if a*d - b*c != 0:
                x = (b*f - e*d) / (a*d - b*c)
                y = (e*c - a*f) / (a*d - b*c)
                if x == int(x) and y == int(y):
                    star.append([int(x), int(y)])
    min_x = star[0][0]
    max_x = star[0][0]
    min_y = star[0][1]
    max_y = star[0][1]
    for x, y in star:
        if min_x > x:
            min_x = x
        if max_x < x:
            max_x = x
        if min_y > y:
            min_y = y
        if max_y < y:
            max_y = y
    x_range = max_x - min_x + 1
    y_range = max_y - min_y + 1
    board = [['.']*x_range for _ in range(y_range)]
    for x, y in star:
        x = x-min_x
        y = y-max_y
        board[-y][x] = '*'
    for ans in board:
        answer.append("".join(ans))
    return answer