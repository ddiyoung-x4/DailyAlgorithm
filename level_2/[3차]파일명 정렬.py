import re

def solution(files):
    temp_files = []
    
    for file in files:
        a, b = re.search('\d+', file).span()
        head = file[:a]
        number = file[a:b]
        tail = file[b:]
        temp_files.append([head, number, tail])
    
    # HEAD 같을 경우, NUMBER 0 무시
    temp_files.sort(key=lambda x:int(x[1]))
    # HEAD 사전 정렬
    temp_files.sort(key=lambda x:x[0].lower())
    # HEAD, NUMBER 같을 경우, 주어진 순서 유지
    # print(temp_files)
    answer = [''.join(temp_files[i]) for i in range(len(temp_files))]

    return answer