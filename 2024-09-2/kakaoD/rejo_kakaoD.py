def solution(coin, cards):
    answer = 0
    
    # 접근법 1. 
    # 그리디 : 당장 n + 1을 만족하는 카드 쌍을 무작정 많이 사두는 것보다 더 효율적인 방법이 존재함. 
    # 예를 들면, (초반에 받은 카드 1장 + k라운드에 뽑은 카드 1장 == n + 1) 2쌍 으로 2라운드 버티기 가능
    
    # 접근법 2.
    # 탑다운 DP : 코인을 ? 개 소모했을 때 최대 몇 라운드까지 버틸 수 있는지를 DP에 상태 표시
    # 그리디 접근법보다 더 다양한 경우를 고려 가능함. 공간 복잡도 또한 만족함.
    
    n = len(cards)
    rounds = n // 3
    
    # dp[i][j] : i라운드에 코인 j 개를 가지고 있을 때, 앞으로 최대 dp[i][j] 개 라운드를 버틸 수 있음.
    # -1 : 도달 불가능한 상태
    dp = [[-1 for _ in range(coin+1)] for _ in range(rounds + 1)]
    dp[0][coin] = 0 # 1라운드에 코인 coin 개를 가지고 있을 때는 도달 가능한 상태.
    for i in range(n // 3 - 1):
        for j in range(i + 1, n // 3): 
            # 초반에 가지는 n // 3 개의 카드 중에서 n + 1을 만족하는 카드 쌍이 있는지 확인
            if cards[i] + cards[j] == n + 1:
                dp[0][coin] += 1 # 그 카드 쌍으로 1라운드 씩 버틸 수 있음!
    
    # 1라운드에 코인을 소모하지 않고 dp[0][coin] 라운드를 버틸 수 있다면,
    # 2라운드에 코인을 소모하지 않았을 땐 dp[0][coin] - 1 라운드를 더 버틸 수 있고,
    # 3라운드에 코인을 소모하지 않았을 땐 dp[0][coin] - 2 라운드를 더 버틸 수 있고...
    # 앞으로 코인을 소모하지 않을 때의 도달 가능한 상태를 전파한다.
    for k in range(dp[0][coin]): dp[k+1][coin] = dp[0][coin] - 1 - k
    
    for i in range(rounds + 1):
        # 다음 라운드 도달
        answer += 1
        
        # 마지막 라운드에 도착했다면 종료한다.
        if i == rounds: break
        
        # c : i라운드에 받는 카드 
        # p : i라운드 이전에, c와 합했을 때 n + 1을 만족하는 카드
        for c in range(rounds + (i * 2), rounds + (i * 2) + 2):
            for p in range(rounds + (i * 2)):
                if cards[c] + cards[p] == n + 1:
                    if p < rounds: # p가 1라운드 이전에 받은 카드라면 이미 보유 중. 코인 1개 소모 (c 구매)
                        for j in range(1, coin + 1):
                            if dp[i][j] >= 0: # i라운드에 코인 j개를 소유할 수 있다면
                                dp[i][j-1] = max(dp[i][j-1], dp[i][j] + 1) # 코인 1개 소모하고 1라운드 추가
                    else: # p는 1라운드부터 받은 카드. 이전에 구매 했어야 하므로 코인 2개 소모 (c와 p 구매)
                        for j in range(2, coin + 1):
                            if dp[i][j] >= 0:
                                dp[i][j-2] = max(dp[i][j-2], dp[i][j] + 1)
        # NOTE 
        # for j in range(1, coin + 1) 을 역순으로 진행하면 값이 계속 전파되는 논리 오류 발생.
        # 1부터 시작해야 제일 코인이 없을 때부터 시작해서 정확한 전파가 가능함.
                                
        if cards[rounds + (i * 2)] + cards[rounds + (i * 2) + 1] == n + 1: # 받은 두 개가 n + 1을 만족한다면
            for j in range(2, coin + 1):
                if dp[i][j] >= 0:
                    dp[i][j-2] = max(dp[i][j-2], dp[i][j] + 1)
        
        # 현재 라운드에서, 각 코인마다 버틸 수 있는 라운드가 있다면 다음 라운드로 전파하여 도달 가능함을 알리기
        for j in range(coin + 1):
            for k in range(dp[i][j]):
                if i + 1 + k > rounds: break
                dp[i+1+k][j] = dp[i][j] - 1 - k
        
        # 카드를 전부 구매했지만, 1라운드도 버틸 수 없다면 종료
        survived = 0
        for j in range(coin + 1):
            if dp[i][j] > 0:
                survived = 1
                break
                
        if survived == 0:
            break
    
    return answer
