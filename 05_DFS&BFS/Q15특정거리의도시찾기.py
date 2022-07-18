# 2022-07-16 16:06 ~ 38

# DFS 사용하려다가 실패!
# 도시 x를 시작점으로 BFS를 수행 -> 모든 도시까지의 최단 거리 계산 -> 각 최단 거리 확인하며 k인 경우 출력
# 방문하지 않은 도시라면 최단 시간 갱신
# '모든 도로의 거리는 1'이라는 조건 덕분에 BFS로 간단히 해결 가능. 노드 개수 n (최대 300,000) 간선 개수 m (최대 1,000,000) -> 시간 복잡도 O(n + m)으로 동작

# n, m, k, x = map(int, input().split())
# graph = [[] for _ in range(n + 1)]
# for _ in range(m):
#   a, b = map(int, input().split())
#   graph[a].append(b)

# visited = [False] * (n + 1)
# result = []

# def dfs(graph, x, visited, cnt, result):
#   global k

#   visited[x] = True
#   cnt += 1
#   if cnt == k:
#     result.append(x)
#     print(cnt, result)

#   else:
#     if not graph[x]:
#       cnt -= 1
#     for node in graph[x]:
#       if not visited[node]:
#         dfs(graph, node, visited, cnt, result)
#       else:
#         cnt -= 1

# dfs(graph, x, visited, 0, result)
# print(result)

from collections import deque

# 도시의 개수, 도로의 개수, 거리 정보, 출발 도시 번호
n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]

# 모든 도로 정보 입력받기
for _ in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)

# 모든 도시에 대한 최단 거리 초기화
distance = [-1] * (n + 1)
distance[x] = 0 # 출발 도시까지의 거리는 0으로 설정

# 너비 우선 탐색(BFS) 수행
q = deque([x])
while q:
  now = q.popleft()
  # 현재 도시에서 이동할 수 있는 모든 도시를 확인
  for next_node in graph[now]:
    # 아직 방문하지 않은 도시라면
    if distance[next_node] == -1:
      # 최단 거리 갱신
      distance[next_node] = distance[now] + 1
      q.append(next_node)

# 최단 거리가 K인 모든 도시의 번호를 오름차순으로 출력
check = False
for i in range(1, n + 1):
  if distance[i] == k:
    print(i)
    check = True

if check == False:
  print(-1)