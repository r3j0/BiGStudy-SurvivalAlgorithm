# 15996 : 팩토리얼 나누기
import sys
input = sys.stdin.readline

N, A = map(int, input().split())
k = 0
power = A # A의 제곱수

# N!에 포함되어 있는 A의 개수를 구하기 위해서, A의 제곱수를 나눈 몫을 누적하여 구한다.
while N >= power: # N이 A의 제곱수보다 크거나 같을 때 반복
    k += N // power # N을 A제곱수로 나눈 몫을 k에 더하고
    power *= A      # A의 제곱수에 A를 한 번 더 곱함

print(k)