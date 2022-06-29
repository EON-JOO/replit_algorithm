# 2022-06-28 02:22 ~ 03:04
n, m = map(int, input().split())
a, b, d = map(int, input().split())
map = [list(map(int, input().split())) for _ in range(n)]

da = [-1, 0, 1, 0] # 북서남동 (0, 3, 2, 1)
db = [0, -1, 0, 1]
dir = [0, 3, 2, 1]
now_dir = dir.index(d)
save_dir = now_dir
map[a][b] = 2 # 가본 곳은 2

while True:
  now_dir = (now_dir + 1) % 4 # 왼쪽으로 돌아
  na = a + da[now_dir]
  nb = b + db[now_dir]

  if map[na][nb] > 0: # 가봤거나(2) 바다인 경우(1)
    if save_dir == now_dir: # 4방향 모두 확인
      tmp = (now_dir + 2) % 4 # 뒤쪽 방향
      na = a + da[tmp]
      nb = b + db[tmp]
      if map[na][nb] == 1: # 뒤쪽 방향이 바다인 칸이면
        break
      else:
        a, b = na, nb
    else:
      continue
  else: # 안 가본 칸이 있는 경우
    a, b = na, nb
    map[a][b] = 2
    save_dir = now_dir
  print(map)

cnt = 0
for i in range(n):
  for j in range(m):
    if map[i][j] == 2:
      cnt += 1

print(cnt)

# 맞음~~~ 정답~~~
# 굳이 방향을 북서남동으로 안해도 되고 빼기를 했어도 됐음. 4방향 모두 갈 수 없을 때 현재 방향의 dx, dy를 빼도 됌

# 교재 답안
# n, m을 공백으로 구분하여 입력받기
# n, m = map(int, input().split())

# 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
# d = [[0] * m for _ in range(n)]
# 현재 캐릭터의 x 좌표, y 좌표, 방향을 입력받기
# x, y, direction = map(int, input().split())
# d[x][y] = 1 # 현재 좌표 방문 처리

# 전체 맵 정보를 입력 받기
# array = []
# for i in range(n):
#   array.append(list(map(int, input().split())))

# 북, 동, 남, 서 방향 정의
# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]

# 왼쪽을 회전
# def turn_left():
#   global direction
#   direction -= 1
#   if direction == -1:
#     direction = 3

# 시뮬레이션 시작
# count = 1
# turn_time = 0
# while True:
#   # 왼쪽으로 회전
#   turn_left()
#   nx = x + dx[direction]
#   ny = y + dy[direction]
#   # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우 이동
#   if array[nx][ny] == 0 and d[nx][ny] == 0:
#     d[nx][ny] = 1
#     x, y = nx, ny
#     count += 1
#     turn_time = 0
#     continue
#   #회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
#   else:
#     turn_time += 1
#   # 네 방향 모두 갈 수 없는 경우
#   if turn_time == 4:
#     nx = x - dx[direction]
#     ny = y - dy[direction]
#     # 뒤로 갈 수 있다면 이동하기
#     if array[nx][ny] == 0:
#       x, y = nx, ny
#     # 뒤가 바다로 막혀있는 경우
#     else:
#       break
#     turn_time = 0

# print(count)