def solution(record):
    answer = []
    id = {}
    for i in range(len(record)):
        msg = record[i].strip().split()
        if msg[0] == "Leave":
            continue
        id[msg[1]] = msg[2]
    # print(id)
    for i in range(len(record)):
        msg = record[i].strip().split()
        if msg[0] == "Enter":
            answer.append(f"{id[msg[1]]}님이 들어왔습니다.")
        elif msg[0] == "Leave":
            answer.append(f"{id[msg[1]]}님이 나갔습니다.")
    return answer