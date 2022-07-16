# 2022-07-16 03:42 ~ 03:51
#            13:51 ~ 14:58

# 구현 실패..!
# 꼬리가 따라가는 것을 구현 못함

# 보드를 2차원 리스트로 구현, 방향 정보 dxdy 테크닉 사용(회전), 꼬리 및 몸통 정보를 리스트에 담아서 꼬리를 pop으로 제거하는 방식으로 구현

# from collections import deque

# n = int(input()) # 보드의 크기
# board = [[0] * n for _ in range(n)]
# board[0][0] = 1 # 1행 1열에는 사과 x, 뱀 위치

# k = int(input()) # 사과 개수
# # 사과 위치에 -1 입력
# for _ in range(k):
#   x, y = map(int, input().split())
#   board[x - 1][y - 1] = -1

# l = int(input()) # 뱀의 방향 변환 횟수
# direction = deque() # 뱀의 방향 변환 정보
# for _ in range(l):
#   direction.append(tuple(input().split()))

# dx = [0, 1, 0, -1]
# dy = [1, 0, -1, 0]
# now_dir = 0 # 현재 방향 오른쪽
# t, dir = direction.popleft()
# x, y = 0, 0
# tx, ty = 0, 0 # 꼬리 위치

# res = 0 # 게임 진행 시간
# while True:
#   if res == int(t): # 방향을 바꿀 시간이면
#     if dir == 'D': # 오른쪽으로 90도 회전
#       now_dir = (now_dir + 1) % 4
#     else: # 왼쪽으로 90도 회전
#       now_dir = (now_dir + 3) % 4

#     if not direction:
#       t, dir = direction.popleft()

#   nx, ny = x + dx[now_dir], y + dy[now_dir]
#   # 보드 범위 벗어나면
#   if nx < 0 or nx >= n or ny <= 0 or ny >= n:
#     break

#   # 자기 자신의 몸과 부딪히면
#   if board[nx][ny] == 1:
#     break

#   # 이동한 칸에 사과가 있다면, 사과 없애고 꼬리 이동 x
#   if board[nx][ny] == -1:
#     print('tail: ', tx, ty)
#     x, y = nx, ny
#     board[x][y] = 1
#     res += 1
#     continue
#   else: # 사과 없으면, 꼬리 이동
#     board[tx][ty] = 0
#     x, y = nx, ny
#     tx, ty = tx + dx[now_dir], ty + dy[now_dir]
#     board[x][y] = 1
#     res += 1
#     continue

# print(res + 1)

# 교재 답안
n = int(input())
k = int(input())
data = [[0] * (n + 1) for _ in range(n + 1)] # 맵 정보
info = [] # 방향 회전 정보

# 맵 정보(사과가 있는 곳은 1로 표시)
for _ in range(k):
  a, b = map(int, input().split())
  data[a][b] = 1

# 방향 회전 정보 입력
l = int(input())
for _ in range(l):
  x, c = input().split()
  info.append((int(x), c))

# 처음에는 오른쪽을 보고 있으므로 (동남서북)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def turn(direction, c):
  if c == 'L':
    direction = (direction - 1) % 4
    # 여기서 -1 % 4 = 3 임!
  else:
    direction = (direction + 1) % 4
  return direction

def simulate():
  x, y = 1, 1 # 뱀의 머리 위치
  data[x][y] = 2 # 뱀이 존재하는 위치는 2로 표시
  direction = 0 # 처음에는 동쪽을 보고 있음
  time = 0 # 시작한 뒤에 지난 '초' 시간
  index = 0 # 다음에 회전할 정보
  q = [(x, y)] # 뱀이 차지하고 있는 위치 정보(꼬리가 앞쪽)
  while True:
    nx = x + dx[direction]
    ny = y + dy[direction]

    # 맵 범위 안에 있고, 뱀의 몸통이 없는 위치라면
    if nx > 0 and nx <=n and ny > 0 and ny <= n and data[nx][ny] != 2:
      # 사과가 없다면 이동 후 꼬리 제거
      if data[nx][ny] == 0:
        data[nx][ny] = 2
        q.append((nx, ny))
        px, py = q.pop(0)
        data[px][py] = 0
      # 사과가 있다면 이동 후 꼬리 그대로 두기
      if data[nx][ny] == 1:
        data[nx][ny] = 2
        q.append((nx, ny))
    # 벽이나 뱀의 몸통과 부딪혔다면
    else:
      time += 1
      break
    x, y = nx, ny # 다음 위치로 머리를 이동
    time += 1
    if index < l and time == info[index][0]: # 회전할 시간인 경우 회전
      direction = turn(direction, info[index][1])
      index += 1
  return time

print(simulate())