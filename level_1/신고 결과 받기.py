def solution(id_list, report, k):
    answer = [0] * len(id_list)
    
    report_dict = {}
    
    for msg in set(report):
        userID, reportID = msg.split(' ')
        report_dict[reportID] = report_dict.get(reportID, []) + [userID]
    
    # for msg in set(report):
    #     userID, reportID = msg.split(' ')
    #     if len(report_dict[reportID]) >= k:
    #         answer[id_list.index(userID)] += 1
    for key in report_dict.keys():
        if len(report_dict[key]) >= k:
            for userID in report_dict[key]:
                answer[id_list.index(userID)] += 1
                
    return answer