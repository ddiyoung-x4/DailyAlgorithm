
def solution(msg):
    
    answer = []
    # 1
    index_dict = {}
    for i in range(26):
        index_dict[chr(i+ord('A'))] = i+1
        
    while True:
        if msg in index_dict.keys():
            answer.append(index_dict[msg])
            break
        
        for i in range(1, len(msg)+1):
            # 2
            if msg[0:i] not in index_dict.keys():
                answer.append(index_dict[msg[0:i-1]])
                # 4
                index_dict[msg[0:i]] = len(index_dict) + 1
                # 3
                msg = msg[i-1:]
                break

    return answer