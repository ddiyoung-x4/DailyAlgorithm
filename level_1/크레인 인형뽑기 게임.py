def solution(board, moves):
    answer = 0
    stack = []
    
    for move in moves:
        for i in range(len(board[0])):
            if board[i][move-1]:
                stack.append(board[i][move-1])
                board[i][move-1] = 0
                if len(stack) != 1 and stack[-1] == stack[-2]:
                    stack.pop()
                    stack.pop()
                    answer += 2
                break
    
        
    return answer