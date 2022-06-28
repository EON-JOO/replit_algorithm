# 2022-06-28 00:01 ~ 00:21

loc = str(input())
grid = [[0 for _ in range(9)] for _ in range(9)]

x = int(ord(loc[0]) - 96)
y = int(loc[1])
cnt = 0

dx = [2, 2, -2, -2, 1, -1, 1, -1]
dy = [1, -1, 1, -1, 2, 2, -2, -2]

for i in range(8):
  nx = x + dx[i]
  ny = y + dy[i]

  if 0 < nx <= 8 and 0 < ny <= 8:
    grid[nx][ny] = 1

for i in range(1, 9):
  for j in range(1, 9):
    if grid[i][j] == 1:
      cnt += 1

print(cnt)

# 좀더 까다롭게 문제를 출제한다면 입력 문자가 열과 행이 아닌 1a와 같은 행과 열 형태로 들어왔을 때의 예외 처리를 요구할 수도 있음 -> 다양한 구현 유형에 대비하기 위해서 파이썬 문법을 자유롭게 사용할 수 있도록 훈련하는 것이 중요
# 마찬가지로 입력 변수를 받는 것을 구현하는데 시간이 걸림 -> 연습 많이 필요

# 교재 답안
# '상하좌우' 문제에서는 dx, dy 리스트를 선언하여 이동할 방향을 기록할 수 있도로 했음. 이번 소스코드에서는 steps 변수가 dx와 dy 변수의 기능을 대신하여 수행 -> 2가지 형태 모두 자주 사용되므로 참고

# # 현재 나이트의 위치 입력받기
# input_data = input()
# row = int(input_data[1])
# column = int(ord(input_data[0])) - int(ord('a')) + 1

# # 나이트가 이동할 수 있는 8가지 방향 정의
# steps = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]

# # 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
# result = 0
# for step in steps:
#   # 이동하고자 하는 위치 확인
#   next_row = row + step[0]
#   next_column = column + step[1]
#   # 해당 위치로 이동이 가능하다면 카운트 증가
#   if next_row >= 1 and next_row <= 8 and next_column >= 1 and next_column <= 8:
#     result += 1

# print(result)
# # 이 문제는 굳이 grid 안 구현해도 됨 (수직1수평2, 수평1수직2의 경우가 없어서 같은 곳으로 가는 중복 경우가 발생하지 않으므로 그냥 카운트해도 됨)