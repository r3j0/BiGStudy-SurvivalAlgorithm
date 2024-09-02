# 10835 : 카드게임

# 2차원 배열 DP 를 사용하여, 
# (1) 왼쪽 카드만 버리거나 (i, j) -> (i+1, j)
# (2) 왼쪽 카드와 오른쪽 카드를 모두 버리거나 (i, j) -> (i+1, j+1)
# (3) 오른쪽 카드만 버리고 오른쪽 카드의 점수를 얻거나 (i, j) -> (i, j+1)
# 에 대해 얻을 수 있는 최대 점수를 계산한다.

# 3번 행동을 할 수 없을 때 (왼쪽 카드 수가 오른쪽 카드 수가 더 높거나 같을 떄)
# DP 배열에서 오른쪽으로 진행할 수 없음을 유의한다. 
# 방문 처리를 통해 등장할 수 있는 상태인지를 판단한다.

import sys
input = sys.stdin.readline

n = int(input().rstrip())
arrA = list(map(int, input().rstrip().split()))
arrB = list(map(int, input().rstrip().split()))

dp = [[0 for _ in range(n+1)] for _ in range(n+1)]
vis = [[0 for _ in range(n+1)] for _ in range(n+1)]
vis[0][0] = 1
for i in range(n):
  lock = 0
  for j in range(n):
    if vis[i][j] == 1: 
      vis[i+1][j] = 1
      dp[i+1][j] = max(dp[i+1][j], dp[i][j])
      
      vis[i+1][j+1] = 1
      dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j])
    
    if arrA[i] > arrB[j] and vis[i][j] == 1:
      dp[i][j+1] = max(dp[i][j+1], dp[i][j] + arrB[j])
      vis[i][j+1] = 1

ans = 0
for d in dp: ans = max(ans, max(d))
print(ans)
