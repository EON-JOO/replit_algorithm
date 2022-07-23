# 2022-07-23 18:50 ~ 19:10
# 2022-07-24 01:15 ~ 01:26

# 시간초과... 사실상 O(n^2)의 for문이 주요 코드가 된 것 같음..

# n, k = map(int, input().split())
# data = [list(map(int, input().split())) for _ in range(n)]
# s, x, y = map(int, input().split())

# tmp = [[0] * n for _ in range(n)]
# for i in range(n):
#   for j in range(n):
#     tmp[i][j] = data[i][j]

# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]


# # 바이러스 퍼뜨리기
# def virus(x, y, v):
#   for l in range(4):
#     nx, ny = x + dx[l], y + dy[l]
#     if nx >= 0 and nx < n and ny >= 0 and ny < n and tmp[nx][ny] == 0:
#       tmp[nx][ny] = v
  

# # DFS
# def dfs(t):
#   global s, k
  
#   if t == s:
#     return
  
#   for v in range(1, k + 1):
#     for i in range(n):
#       for j in range(n):
#         if data[i][j] == v:
#           virus(i, j, v)

#   for i in range(n):
#     for j in range(n):
#       data[i][j] = tmp[i][j]
#   dfs(t + 1)

# dfs(0)
# print(tmp[x - 1][y - 1])

# 교재 답안
# BFS는 상하좌우에 빈공간 있으면 한번에 전진하는 알고리즘 -> 낮은 번호부터 순서대로 증식하는 방식으로 구현
# 초기에 큐에 원소를 삽입할 때 낮은 바이러스 번호부터 삽입 -> BFS 수행하며 방문하지 않은 위치를 차례대로 방문

from collections import deque

n, k = map(int, input().split())

graph = [] # 전체 보드 정보를 담는 리스트
data = [] # 바이러스에 대한 정보를 담는 리스트

for i in range(n):
  # 보드 정보를 한 줄 단위로 입력
  graph.append(list(map(int, input().split())))
  for j in range(n):
    # 해당 위치에 바이러스가 존재하는 경우
    if graph[i][j] != 0:
      # (바이러스 종류, 시간, 위치x, 위치y) 삽입
      data.append((graph[i][j], 0, i, j))

# 정렬 이후에 큐로 옮기기 (낮은 번호의 바이러스가 먼저 증식)
data.sort()
q = deque(data)

target_s, target_x, target_y = map(int, input().split())

# 바이러스가 퍼져나갈 수 있는 4가지 위치
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

# BFS 진행
while q:
  virus, s, x, y = q.popleft()
  # 정확히 s초가 지나거나, 큐가 빌 때까지 반복
  if s == target_s:
    break
  # 현재 노드에서 주변 4가지 위치를 각각 확인
  for i in range(4):
    nx, ny = x + dx[i], y + dy[i]
    # 해당 위치로 이동할 수 있는 경우
    if nx >= 0 and nx < n and ny >= 0 and ny < n:
      # 아직 방문하지 않은 위치라면, 그 위치에 바이러스 넣기
      if graph[nx][ny] == 0:
        graph[nx][ny] = virus
        q.append((virus, s + 1, nx, ny))

print(graph[target_x - 1][target_y - 1])