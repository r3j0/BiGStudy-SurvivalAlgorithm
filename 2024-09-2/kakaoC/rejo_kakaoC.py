from bisect import bisect_right, bisect_left

def solution(dice):
    # 접근법 1. 백트래킹
    # 주사위 고르는 데에 252 * 6**10 까지 가서 순열을 만들어야 함.
    # 경우의 수가 100억이 넘어 단순 백트래킹으로 푸는 데에는 한계가 있음.
    
    # 접근법 2. 백트래킹 + 이분 탐색 + 정렬 + 누적 합 + 비트마스킹
    # 1. 10개 주사위 중에서 5개 주사위를 고르는 경우의 수는 252개이고,
    #    5개 주사위가 만들 수 있는 합의 개수는 6**5 (7776) 개이므로, 
    #    주사위를 고르고 만들 수 있는 합의 개수를 전부 저장해 놓는 것은 가능하다!
    # 2. 백트래킹을 이용해 5개 주사위를 고르고, 그 주사위로 만들 수 있는 합을 전부 구한 뒤 저장한다.
    # 3. 합한 값이 중복될 수 있으므로, 딕셔너리를 통해 특정 주사위 조합에서 나오는 합과 그 합이 등장하는 횟수를 저장한다.
    # 4. 주사위 조합은, 상대방이 가지게 되는 주사위 조합을 쉽게 구하기 위함과 관리 편의성을 위해 비트마스킹으로 관리한다.
    # 5. 5개 주사위 조합을 하나씩 고르고, 나올 수 있는 합을 하나씩 고르면서, 
    #    상대 주사위 조합의 합에서 A 합보다 적게 나오는 경우의 수를 누적합으로 구해야 한다.
    # 6. 딕셔너리의 value 를 따로 분리해 누적합으로 만들어 놓고, key 도 분리하여 이분탐색 용으로 사용한다.
    #    (특정 A 합보다 작고 최대한 큰 합 이분 탐색으로 구하면, 특정 A 합보다 작은 합이 나올 경우의 수를 누적합으로 구한다.)
    # 7. 승리 횟수가 가장 높은 주사위 조합을 구한다.
    
    sumsTuple = [{} for _ in range(1 << len(dice))] # 주사위 조합에서 만들 수 있는 합의 개수 튜플, 인덱스는 비트마스킹
    
    # 주사위 조합에서 나올 수 있는 합 백트래킹
    def backtrackingSums(now, arrIdx, diceList, diceIdx):
        if arrIdx == len(dice) // 2:
            if sumsTuple[diceIdx].get(now, -1) == -1: sumsTuple[diceIdx][now] = 1
            else: sumsTuple[diceIdx][now] += 1
            return
        
        for i in range(6):
            backtrackingSums(now + dice[diceList[arrIdx]][i], arrIdx + 1, diceList, diceIdx)
            
    # 주사위 조합 백트래킹
    def backtrackingDice(now, start):
        if len(now) == len(dice) // 2:
            nowIdx = 0 # 주사위 조합 인덱스
            for element in now: nowIdx |= (1 << element)
            backtrackingSums(0, 0, now, nowIdx)
            return
        
        for i in range(start, len(dice)):
            now.append(i)
            backtrackingDice(now, i + 1)
            now.pop()
        
    backtrackingDice([], 0)
                                           
    # 이분 탐색을 위한 key 정렬
    for i in range(1 << len(dice)):
        sumsTuple[i] = dict(sorted(sumsTuple[i].items())) 
    
    # key, value 분리 및 value 누적합 배열 만들기                                           
    sumsKey = [list(sumsTuple[i].keys()) for i in range(1 << len(dice))]
    sumsValue = [list(sumsTuple[i].values()) for i in range(1 << len(dice))]

    sumsPrefixValue = [list(sumsValue[i]) for i in range(1 << len(dice))]
    for i in range(1 << len(dice)): 
        for j in range(1, len(sumsPrefixValue[i])):
            sumsPrefixValue[i][j] += sumsPrefixValue[i][j-1]
    
    answer = []
    answerValue = 0
    for a in range(1 << len(dice)):
        winCnt = 0
        for k in range(len(sumsKey[a])):
            # b의 주사위 조합은 a의 비트마스킹 반전
            b = (~a) & ((1 << len(dice)) - 1)

            # 이분 탐색을 이용한 sumsKey[a][k] 보다 작지만 가장 큰 B합 구하기
            findALower = bisect_left(sumsKey[b], sumsKey[a][k]) - 1
            if findALower < 0: continue

            # A 합이 등장한 횟수 * B 합보다 작거나 같은 합들이 등장한 횟수
            winCnt += sumsValue[a][k] * sumsPrefixValue[b][findALower]
        
        if winCnt > answerValue:
            answerValue = winCnt

            # answer 배열 만들기
            answer = []
            mask = 1
            maskCnt = 1
            while mask < 1 << len(dice):
                if a & mask != 0: answer.append(maskCnt)
                mask <<= 1
                maskCnt += 1
    
    return answer
    
