# 2022-07-18 18:07 ~ 18:15

from collections import deque

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)

distance = [-1] * (n + 1)
distance[x] = 0

def bfs(graph):
  q = deque([x])

  while q:
    now_node = q.popleft()
    for next_node in graph[now_node]:
      if distance[next_node] == -1:
        distance[next_node] = distance[now_node] + 1
        q.append(next_node)

bfs(graph)

tmp = False
for i in range(n + 1):
  if distance[i] == k:
    print(i)
    tmp = True

if tmp == False:
  print(-1)