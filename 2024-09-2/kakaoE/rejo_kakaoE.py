def solution(n, tops):
    answer = 0
    dp = [[0, 0] for _ in range(n)]
    # dp[i][0] : i번째 정삼각형 줄까지 △, ◇, △▽ 를 사용했을 경우
    # dp[i][1] : i번째 정삼각형 줄에 ▽△ 를 사용했을 경우 (다음 정삼각형 칸까지 차지할 경우)
    
    if tops[0] == 0: dp[0] = [2, 1]
    else: dp[0] = [3, 1]
    
    for i in range(1, n):
        if tops[i] == 0:
            dp[i] = [((dp[i-1][0] * 2) + (dp[i-1][1])) % 10007, (dp[i-1][0] + dp[i-1][1]) % 10007]
        else:
            dp[i] = [((dp[i-1][0] * 3) + (dp[i-1][1] * 2)) % 10007, (dp[i-1][0] + dp[i-1][1]) % 10007]
    
    answer = sum(dp[n-1]) % 10007
    
    return answer
