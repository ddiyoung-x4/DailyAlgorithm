def solution(word):
    answer = 0
    alpha = ['A', 'E', 'I', 'O', 'U']
    plus = [781,156,31,6,1]
    for i, alp in enumerate(word):
        if alp == 'A':
            answer += 1
        else:
            answer += plus[i]*alpha.index(alp) + 1
        
        
    return answer


# A 1
# 5자리수
# AAAAA ~ AAAAU 5개
# AAAEA ~ AAAEU 5개 ... AAAUA ~ AAAUU 5개 = 5 * 5 개
# AAE.., AAI.., AAO.., AAU.. -> 5 * 5 * 5개
# AA..., -> 5 * 5 * 5 * 5 개
# 4자리수 = AAAA ~ AUUU 5 * 5 * 5 개
# 3자리수 = AAA ~ AUU = 5 * 5 개
# 2자리수 = AA, AE, ... = 5개
# 1자리수 = A 1개
# E


# EA
# 2자리수, EA 1개
# 3자리수, EAA ~ EAU 5개
# 4자리수, EAAA ~ EAUU 25개
# 5자리수, EAAAA ~ EAUUU 125개
# EE
# 2자리수, EE 1개
# 3자리수, EEA ~ EEU 5개
# 4자리수, EEAA ~ EEUU 5개
# 5자리수, EEAAA ~ EEUUU 125개
# 1 + 5 + 25 + 125
# EI

# EIA

# 3자리수, EIA 1개
# 4자리수, EIAA ~ EIAU 5개
# 5자리수, EIAA ~ EIUU 25개
# 1 + 5 + 25
# EIE
# 3자리수, EIE 1개
# 4자리수, EIEA ~ EIEU 5개
# 5자리수, EIEAA ~ EIEUU 25개
# 1 + 5 + 25
# EII
# 1 + 5 + 25
# EIO

# A 1 
# AA 2
# AA
# 1 + 5 + 25
# AAE
# 1 + 5 + 25
# AAI