# 2072 : 오목
import sys
input = sys.stdin.readline

n = int(input().rstrip())
order = [list(map(int, input().rstrip().split())) for _ in range(n)]
maps = [[-1 for _ in range(20)] for _ in range(20)]

#     가로      세로    대각선 \  대각선 /
dx = [[-1, 1], [0, 0], [-1, 1], [-1, 1]]
dy = [[0, 0], [-1, 1], [1, -1], [-1, 1]]

def check5mok(x, y, who):
  for d in range(4):
    cnt = 1
    for l in range(2):
      nx = x + dx[d][l]
      ny = y + dy[d][l]
      while 1 <= nx <= 19 and 1 <= ny <= 19 and maps[nx][ny] == who:
        cnt += 1
        nx += dx[d][l]
        ny += dy[d][l]

    if cnt == 5: return True
    
  return False

turn = 0
time = 1
done = -1
for o in order:
  maps[o[0]][o[1]] = turn
  if check5mok(o[0], o[1], turn):
    done = time
    break
  turn ^= 1
  time += 1

print(done)
