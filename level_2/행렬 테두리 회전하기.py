# def solution(rows, columns, queries):
#     answer = []
#     mat = [[0] * columns for _ in range(rows)]
#     for i in range(rows):
#         for j in range(columns):
#             mat[i][j] = i*columns + j+1
        
#     for lt_row, lt_col, rb_row, rb_col in queries:
        
#         lt_row -= 1
#         lt_col -= 1
#         rb_row -= 1
#         rb_col -= 1
        
#         rt = mat[lt_row][rb_col]
#         MIN = rt
        
#         # ->
#         for j in range(rb_col, lt_col, -1):
#             mat[lt_row][j] = mat[lt_row][j-1]
#             MIN = min(MIN, mat[lt_row][j])   
#         # top
#         for i in range(lt_row, rb_row):
#             mat[i][lt_col] = mat[i+1][lt_col]
#             MIN = min(MIN, mat[i][lt_col])
#         # <-
#         for j in range(lt_col, rb_col):
#             mat[rb_row][j] = mat[rb_row][j+1]
#             MIN = min(MIN, mat[lt_row][j])
#         # bottom
#         for i in range(rb_row, lt_row, -1):
#             mat[i][rb_col] = mat[i-1][rb_col]
#             MIN = min(MIN, mat[i][rb_col])
#         mat[lt_row + 1][rb_col] = rt
#         answer.append(MIN)
#     return answer

def solution(rows, columns, queries):
    answer = []
    table = [[0] * columns for _ in range(rows)]
    for i in range(rows):
        for j in range(columns):
            table[i][j] = i*columns + j+1
    
    for query in queries:
        query = [x-1 for x in query] # 0부터 시작하는 인덱스에 맞춰 1씩 빼줌
        tmp = table[query[0]][query[1]] # 왼쪽 위 값 저장
        small = tmp
        
        # left
        for i in range(query[0]+1, query[2]+1):
            table[i-1][query[1]] = table[i][query[1]]
            small = min(small, table[i][query[1]])
        # bottom
        for i in range(query[1]+1, query[3]+1):
            table[query[2]][i-1] = table[query[2]][i]
            small = min(small, table[query[2]][i])
        # right
        for i in range(query[2]-1, query[0]-1, -1):
            table[i+1][query[3]] = table[i][query[3]]
            small = min(small, table[i][query[3]])
        # top
        for i in range(query[3]-1, query[1]-1, -1):
            table[query[0]][i+1] = table[query[0]][i]
            small = min(small, table[query[0]][i])
        table[query[0]][query[1]+1] = tmp
        
        answer.append(small)
    
    return answer