# 2435 : 기상청 인턴 신현수
import sys
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
arr = list(map(int, input().rstrip().split()))

# 슬라이딩 윈도우
# 먼저, 0번째부터 (k-1)번째 요소까지의 합을 구해놓는다.
# 이후 k번째 요소를 더하고 0번째 요소를 빼서 1번째부터 k번째 요소까지의 합을 구하고,
# (k+1)번째 요소를 더하고 1번째 요소를 빼서 2번째부터 (k+1)번째 요소까지의 합을 구하고...
# 이 방식을 (n-1)번째 요소까지 반복하면서 최대연속합을 구한다.

now_sum = sum([arr[i] for i in range(k)])
max_sum = now_sum
for i in range(k, n):
  now_sum += arr[i] - arr[i-k]
  max_sum = max(max_sum, now_sum)

print(max_sum)
