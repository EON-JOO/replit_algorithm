# 2022-06-02 16:15 ~ 30
# 2022-06-16 03:42 ~ 48

n = int(input())
move = input().split()

dir = {
  'L': 0,
  'R': 1,
  'U': 2,
  'D': 3
}
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
grid = [[0 for _ in range(n)] for _ in range(n)]
x, y = 0, 0

for next in move:
  nd = dir[next]
  nx, ny = x + dx[nd], y + dy[nd]

  if 0 <= nx < n and 0 <= ny < n:
    x, y = nx, ny
  else:
    continue

print(x+1, y+1)

# 교재 답안
# N을 입력받기
# n = int(input())
# x, y = 1, 1
# plans = input().split()

# # L, R, U, D에 따른 이동 방향
# dx = [0, 0, -1, 1]
# dy = [-1, 1, 0, 0]
# move_types = ['L', 'R', 'U', 'D']

# # 이동 계획을 하나씩 확인
# for plan in plans:
#   # 이동 후 좌표 구하기
#   for i in range(len(move_types)):
#     if plan == move_types[i]:
#       nx = x + dx[i]
#       ny = y + dy[i]
#   # 공간을 벗어나는 경우 무시
#   if nx < 1 or ny < 1 or nx > n or ny > n:
#     continue
#   # 이동 수행
#   x, y = nx, ny

# print(x, y)