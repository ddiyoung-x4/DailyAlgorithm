def str2int(time):
    h = int(time[0:2]) * 3600
    m = int(time[3:5]) * 60
    s = int(time[6:])
    
    return h + m + s

def int2str(time):
    h = time // 3600
    m = (time - h*3600) // 60
    s = time - h*3600 - m*60
    
    answer = str(h).zfill(2) + ':'
    answer += str(m).zfill(2) + ':'
    answer += str(s).zfill(2)
    
    return answer

def solution(play_time, adv_time, logs):
    
    play_time = str2int(play_time)
    adv_time = str2int(adv_time)
    
    dp = [0] * (play_time + 1)
    for log in logs:
        start = str2int(log[:8])
        end = str2int(log[9:])
        
        dp[start] += 1
        dp[end] -= 1
    
    # 각 초마다 시청중인 인원 
    for i in range(1, play_time+1):
        dp[i] = dp[i] + dp[i-1]
    # 누적 시청중인 인원
    for i in range(1, play_time+1):
        dp[i] = dp[i] + dp[i-1]
    
    answer = 0
    max_cnt = dp[adv_time]
    for time in range(1, play_time+1 - adv_time):
        if max_cnt < dp[time+adv_time] - dp[time]:
            max_cnt = dp[time+adv_time] - dp[time]
            answer = time + 1
    
    return int2str(answer)