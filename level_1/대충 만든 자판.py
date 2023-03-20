def solution(keymap, targets):
    answer = []
    
    key_dict = {}
    for keys in keymap:
        for i, key in enumerate(keys):
            if key not in key_dict:
                key_dict[key] = i+1
            else:
                orig = key_dict[key]
                key_dict[key] = min(orig, i+1)
    print(key_dict)
    
    
    for target in targets:
        sum = 0
        for alp in target:
            if alp in key_dict:
                sum += key_dict[alp]
            else:
                sum = -1
                break
        answer.append(sum)
    return answer
