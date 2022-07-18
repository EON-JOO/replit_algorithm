# 2022-07-18 17:25 ~ 18:02

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)

res = [0] * (n + 1)
d = 0

def dfs(graph, v, d):
  if res[v] == 0 or res[v] > d:
    res[v] = d
  for i in graph[v]:
    d += 1
    dfs(graph, i, d)
    d -= 1
  
dfs(graph, x, d)

cnt = 0
for i in range(len(res)):
  if res[i] == k:
    cnt += 1
    print(i)

if cnt == 0:
  print(-1)