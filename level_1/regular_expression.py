import re

def solution(new_id):
    
    new_id = new_id.lower()
    new_id = re.sub('[^a-z]', '', new_id)

    return new_id

print(solution('ABC123'))