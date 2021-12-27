def solution(numbers, hand):
    answer = ''
    phone = [[3,1],[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2],[3,0],[3,2]]
    left_pos = phone[10] # '*'
    right_pos = phone[11] # '#'
    left_hand = 10 # '*'
    right_hand = 11 # '#'
    for i, digit in enumerate(numbers):
        if digit == 1 or digit == 4 or digit == 7:
            left_hand = digit
            left_pos = phone[digit]
            answer += 'L'
        elif digit == 3 or digit == 6 or digit == 9:
            right_hand = digit
            right_pos = phone[digit]
            answer += 'R'
        else:
            # 왼손 거리
            left_dist = abs(phone[digit][0] - left_pos[0]) + abs(phone[digit][1] - left_pos[1])
            # 오른손 거리
            right_dist = abs(phone[digit][0] - right_pos[0]) + abs(phone[digit][1] - right_pos[1])
            
            if left_dist < right_dist:
                left_hand = digit
                left_pos = phone[digit]
                answer += 'L'
            elif left_dist > right_dist:
                right_hand = digit
                right_pos = phone[digit]
                answer += 'R'
            else:
                if hand == 'left':
                    left_hand = digit
                    left_pos = phone[digit]
                    answer += 'L'
                else:
                    right_hand = digit
                    right_pos = phone[digit]
                    answer += 'R'
    return answer