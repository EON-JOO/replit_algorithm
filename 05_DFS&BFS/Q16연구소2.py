# 2022-07-18 18:22 ~ 18:51

# 또 실패..
# 빈 공간에 울타리 설치하는 부분(재귀)이랑 바이러스 퍼뜨릴 때 바이러스 위치마다 함수 호출하는 부분 확인!

n, m = map(int, input().split())
data = []
for _ in range(n):
  data.append(list(map(int, input().split())))
tmp = [[0] * m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
  
# 바이러스 퍼뜨리기
def virus(x, y):
  for i in range(4):
    nx, ny = x + dx[i], y + dy[i]
    # 범위 내 이고 0이면
    if nx >= 0 and nx < n and ny >= 0 and ny < m and tmp[nx][ny] == 0:
      tmp[nx][ny] = 2
      virus(nx, ny)
      

# 안전 영역 크기 구하기
def count_of_safe_area():
  cnt = 0
  for i in range(n):
    for j in range(m):
      if tmp[i][j] == 0:
        cnt += 1
  return cnt


res = 0 # 안전 영역의 최대 크기

def solution(cnt):
  global res
  
  if cnt == 3:
    for i in range(n):
      for j in range(m):
        tmp[i][j] = data[i][j]
    # .copy() : 얕은 복사여서 안돼!

    # 각 바이러스의 위치에서 전파 진행
    for i in range(n):
      for j in range(m):
        if tmp[i][j] == 2:
          virus(i, j)
          
    res = max(res, count_of_safe_area())
    return

  # 빈 공간에 울타리 설치
  for i in range(n):
    for j in range(m):
      if data[i][j] == 0:
        data[i][j] = 1
        cnt += 1
        solution(cnt)
        data[i][j] = 0
        cnt -= 1

solution(0)
print(res)