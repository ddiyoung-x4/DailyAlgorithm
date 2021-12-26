def solution(new_id):
    spec_char = '`~!@#$%^&*()=+/?><,;:[]{}'

    # 1단계
    new_id = new_id.lower()

    # 2단계
    for i in range(len(spec_char)):
        new_id = new_id.replace(spec_char[i], "")

    dot = ['.......', '......', '.....', '....', '...', '..']
    for j in range(len(dot)):
        new_id = new_id.replace(dot[j],".")
        print(new_id)

    # 4단계
    if len(new_id) != 0 and new_id[0] == '.':
        new_id = new_id[1:]
    if len(new_id) != 0 and new_id[-1] == '.':
        new_id = new_id[:-1]
    # 5단계
    if len(new_id) == 0:
        new_id = 'a'
    # 6단계
    if len(new_id) > 15:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id[:-1]
    while(len(new_id) < 3):
        new_id = new_id[:] + new_id[-1]

    return new_id
