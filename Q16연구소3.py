# 2022-07-18 19:06 ~ 19:1

n, m = map(int, input().split())
data = []
for _ in range(n):
  data.append(list(map(int, input().split())))
tmp = [[0] * m for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def virus(x, y):
  for i in range(4):
    nx, ny = x + dx[i], y + dy[i]
    if nx >= 0 and nx < n and ny >= 0 and ny < m:
      if tmp[nx][ny] == 0:
        tmp[nx][ny] = 2
        virus(nx, ny)
        

def check():
  cnt = 0
  for i in range(n):
    for j in range(m):
      if tmp[i][j] == 0:
        cnt += 1
  return cnt

res = 0

def dfs(cnt):
  global res
  
  if cnt == 3:
    # 바이러스 퍼뜨려야 하므로 벽 세운 리스트 복사
    for i in range(n):
      for j in range(m):
        tmp[i][j] = data[i][j]
    for i in range(n):
      for j in range(m):
        if tmp[i][j] == 2:
          virus(i, j)
    res = max(res, check())
    return

  for i in range(n):
    for j in range(m):
      if data[i][j] == 0:
        data[i][j] = 1
        cnt += 1
        dfs(cnt)
        data[i][j] = 0
        cnt -= 1

dfs(0)
print(res)