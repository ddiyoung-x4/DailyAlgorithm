def solution(phone_book):
    answer = True
    
    phone_dict = dict()
    for num in phone_book:
        phone_dict[num] = 1
    for num in phone_book:
        for i in range(1, len(num)):
            if phone_dict.get(num[:i]) is not None:
                return False
            
    return answer