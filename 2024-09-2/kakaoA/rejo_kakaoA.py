def solution(friends, gifts):
    friend_num = len(friends)
    
    table = [[0 for _ in range(friend_num)] for _ in range(friend_num)] # table[i][j] : 친구 i가 친구 j에게 선물을 몇 번 보냈는지
    send = [0 for _ in range(friend_num)] # send[i] : 친구 i가 선물을 몇 번 보냈는지
    receive = [0 for _ in range(friend_num)] # receive[i] : 친구 i가 선물을 몇 번 받았는지

    # 친구 이름을 인덱스화 시켜 배열에 저장하기 쉽도록 한다.
    def friendIndex(name): 
        idx = 0
        for f in friends:
            if f == name:
                return idx
            idx += 1
        
    for g in gifts:
        start, end = g.split()
        startIdx = friendIndex(start) # 친구 이름을 번호로 변환
        endIdx = friendIndex(end)
        
        table[startIdx][endIdx] += 1
        send[startIdx] += 1
        receive[endIdx] += 1
    
    next_receive = [0 for _ in range(friend_num)] # next_receive[i] : 친구 i가 다음 달에 선물을 몇 번 받을지
    
    for start in range(friend_num):
        for end in range(start + 1, friend_num): # 모든 친구들의 선물 관계를 1번씩 체크한다. 중복되지 않도록 end 를 start + 1 부터 시작한다.
            if table[start][end] == table[end][start]: # 서로 보낸 기록이 없거나 보낸 기록이 같을 경우
                start_score = send[start] - receive[start] # 선물 지수 측정
                end_score = send[end] - receive[end]
                
                if start_score > end_score: next_receive[start] += 1 # 선물 지수가 더 높은 친구가 다음 달에 한 번 더 받는다.
                elif start_score < end_score: next_receive[end] += 1
            elif table[start][end] > table[end][start]: next_receive[start] += 1 # 더 많이 보낸 친구가 다음 달에 한 번 더 받는다.
            else: next_receive[end] += 1

    # 다음 달에 가장 많이 받을 친구의 받을 선물 수
    return max(next_receive)
