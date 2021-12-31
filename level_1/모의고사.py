def solution(answers):
    answer = []
    person1 = [1,2,3,4,5]
    person2 = [2,1,2,3,2,4,2,5]
    person3 = [3,3,1,1,2,2,4,4,5,5]
    s = [0, 0, 0]
    for i, data in enumerate(answers):
        if data == person1[i%5]:
            s[0] += 1
        if data == person2[i%8]:
            s[1] += 1
        if data == person3[i%10]:
            s[2] += 1
    
    for i, data in enumerate(s):
        if data == max(s):
            answer.append(i+1)
    return answer