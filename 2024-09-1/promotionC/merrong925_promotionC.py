# 26099 : 설탕 배달 2
import sys
input = sys.stdin.readline

N = int(input().strip()) # kg
bag_count = 0            # 봉지 수

'''
- N이 5의 배수인 경우: N // 5
- N이 5의 배수가 아닌 경우: 5kg 봉지를 사용할 수 없거나, 남은 무게가 5로 나누어 떨어지지 않을 때는, N에서 3kg을 빼고 다시 시도한다. 
                        이 과정을 반복하며, 남은 N이 0이 되면 그때까지 사용한 봉지의 총 개수를 출력한다.
- N이 0보다 작은 경우: 주어진 Nkg을 3kg과 5kg 봉지로 정확하게 만들 수 없다는 의미이므로 -1을 출력한다.
'''
while N >= 0:
    # 5kg 봉지 최대한 많이 사용해야 한다.
    if N % 5 == 0:  # 5의 배수인 경우, 5의 몫을
        bag_count += N // 5
        print(bag_count)
        break
    N -= 3
    bag_count += 1
else:
    print(-1)