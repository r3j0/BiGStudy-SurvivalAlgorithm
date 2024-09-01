# 15996 : 팩토리얼 나누기
import sys
import math
input = sys.stdin.readline

n, a = map(int, input().rstrip().split())

# a가 2일 때를 가정하면,
# 2, 4, 6, 8, 10.. (2의 배수) 에서 2가 1회.
# 4. 8. 16. 20. 24.. (4의 배수) 에서 2가 2회. (2의 배수에서 이미 2가 1회 등장했으므로. 2 - 1 = 1회 등장.)
# 8, 16, 24, 32, 40.. (8의 배수) 에서 2가 3회. (2의 배수, 4의 배수에서 이미 2가 등장함. 3 - 2 = 1회 등장.)
# ...
# 따라서, n을 a**i 로 나눈 몫을 전부 더하면 N! 에서 A가 몇 번 등장하는지 계산 가능

now = a
ans = 0
while now <= n: 
  ans += n // now
  now *= a
print(ans)
