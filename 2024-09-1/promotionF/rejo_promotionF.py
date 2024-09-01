# 16174 : 점프왕 쩰리 (Large)
import sys
from collections import deque
input = sys.stdin.readline

n = int(input().rstrip())
maps = [list(map(int, input().rstrip().split())) for _ in range(n)]

dp = [[0 for _ in range(n)] for _ in range(n)]
dp[0][0] = 1

for i in range(n):
  for j in range(n):
    if dp[i][j] == 1:
      if i + maps[i][j] < n: dp[i + maps[i][j]][j] = 1
      if j + maps[i][j] < n: dp[i][j + maps[i][j]] = 1

print('HaruHaru' if dp[n-1][n-1] == 1 else 'Hing')
