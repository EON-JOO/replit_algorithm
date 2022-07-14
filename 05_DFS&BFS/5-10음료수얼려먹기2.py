# 2022-07-09 15:55 ~ 04:07
# 복습

def dfs(x, y):
  if x < 0 or x >= n or y < 0 or y >= m:
    return False

  if grid[x][y] == 0:
    grid[x][y] = 1

    dfs(x - 1, y)
    dfs(x, y - 1)
    dfs(x + 1, y)
    dfs(x, y + 1)

    return True
    
  return False

n, m = map(int, input().split())
grid = []
for _ in range(n):
  grid.append(list(map(int, input())))

res = 0
for x in range(n):
  for y in range(m):
    if dfs(x, y):
      res += 1

print(res)