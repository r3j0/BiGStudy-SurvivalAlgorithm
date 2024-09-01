# 11816 : 8진수, 10진수, 16진수
import sys
input = sys.stdin.readline

# 수의 앞에 0x가 주어질 경우에는 16진수를 10진수로 변환한다.
# 수의 앞에 0가 주어질 경우에는 8진수를 10진수로 변환한다.
# 그 외에는 그냥 출력한다.
x = input().rstrip()
print(     (int(x, 16)) if (len(x) > 2 and x[:2] == '0x') 
      else (int(x, 8)) if (len(x) > 1 and x[0] == '0') 
      else (x)
     )
