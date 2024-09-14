def solution(friends, gifts):
    friend_num = len(friends)
    table = [[0 for _ in range(friend_num)] for _ in range(friend_num)]
    send = [0 for _ in range(friend_num)]
    receive = [0 for _ in range(friend_num)]
    
    def friendIndex(name):
        idx = 0
        for f in friends:
            if f == name:
                return idx
            idx += 1
        
    for g in gifts:
        start, end = g.split()
        startIdx = friendIndex(start)
        endIdx = friendIndex(end)
        
        table[startIdx][endIdx] += 1
        send[startIdx] += 1
        receive[endIdx] += 1
    
    next_receive = [0 for _ in range(friend_num)]
    
    for start in range(friend_num):
        for end in range(start + 1, friend_num):
            if table[start][end] == table[end][start]:
                start_score = send[start] - receive[start]
                end_score = send[end] - receive[end]
                
                if start_score > end_score: next_receive[start] += 1
                elif start_score < end_score: next_receive[end] += 1
            elif table[start][end] > table[end][start]: next_receive[start] += 1
            else: next_receive[end] += 1

    return max(next_receive)
