# 2022-07-16 16:06 ~ 38

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)

visited = [False] * (n + 1)
result = []

def dfs(graph, x, visited, cnt, result):
  global k

  visited[x] = True
  cnt += 1
  if cnt == k:
    result.append(x)
    print(cnt, result)

  else:
    if not graph[x]:
      cnt -= 1
    for node in graph[x]:
      if not visited[node]:
        dfs(graph, node, visited, cnt, result)
      else:
        cnt -= 1

dfs(graph, x, visited, 0, result)
print(result)