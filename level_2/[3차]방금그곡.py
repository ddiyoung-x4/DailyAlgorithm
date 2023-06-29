import re

def solution(m, musicinfos):
    answer = ''
    
    temp = []
    for music in musicinfos:
        info = music.split(',')
        s_t = int(info[0].split(':')[0])*60 + int(info[0].split(':')[1])
        f_t = int(info[1].split(':')[0])*60 + int(info[1].split(':')[1])
        duration_t = f_t-s_t
        
        replace_list = {'C#':'c', 'D#':'d', 'F#':'f', 'G#':'g', 'A#':'a'}
        
        for key in replace_list.keys():
            m = m.replace(key, replace_list[key])
            info[3] = info[3].replace(key, replace_list[key])
        
        if duration_t > len(info[3]):
            info[3] = info[3] * (duration_t//len(info[3]) + 1)
        info[3] = info[3][:duration_t]

        if re.search(m, info[3]) is not None:
            temp.append([duration_t, info[2]])
    
    temp.sort(key=lambda x:x[0], reverse=True)
    if len(temp) == 0:
        answer = '(None)'
    else:
        answer = temp[0][1]
    return answer