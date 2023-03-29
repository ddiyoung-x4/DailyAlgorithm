def solution(survey, choices):
    answer = ''
    psn_list = ['R', 'T', 'C', 'F', 'J', 'M', 'A', 'N']
    cnt_list = [0] * 8
    
    for i, ab in enumerate(survey):
        if choices[i] < 4:
            cnt_list[psn_list.index(ab[0])] += 4 - choices[i]
        elif choices[i] > 4:
            cnt_list[psn_list.index(ab[1])] += choices[i] - 4
    
    for i in range(4):
        if cnt_list[2*i] >= cnt_list[2*i+1]:
            answer += psn_list[2*i]
        else:
            answer += psn_list[2*i+1]
    
    return answer