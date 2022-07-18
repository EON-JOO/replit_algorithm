# 2022-07-17 15:03 ~ 16:10

# 실패...............
# 시도) 바이러스 위치를 저장하고, 새로운 벽을 추가한 뒤에 바이러스 위치마다 bfs하며 전파. 이후 안전 영역 카운트
# -> 새로운 벽을 추가할 때에도 dfs로 재귀적으로 수행하는 것을 떠올리지 못하고, 구현 실패

# 새로운 벽 추가하면서 벽이 3개 세워지면 바이러스 전파 및 안전 영역 최댓값 계산을 dfs 재귀적으로 수행. 바이러스 전파할 때에는 임시 리스트에 담아 전파 진행.
# 바이러스 전파는 DFS를 통해 재귀적으로 수행

# from collections import deque

# n, m = map(int, input().split())
# graph = []
# for _ in range(n):
#   graph.append(list(map(int, input().split())))


# def virus(copy_graph, start): # BFS로 바이러스 퍼지게 하기
#   dx = [-1, 1, 0, 0] # 상하좌우
#   dy = [0, 0, -1, 1]

#   q = deque()
#   q.append(start)

#   while q:
#     x, y = q.popleft()
#     for i in range(4):
#       nx, ny = x + dx[i], y + dy[i]
#       if copy_graph[nx][ny] == 0:
#         copy_graph[nx][ny] = 2
#         q.append((nx, ny))

#   return copy_graph


# def count_safe_area(graph): # 안전 영역 크기 계산
#   res = 0
#   for i in range(n):
#     for j in range(m):
#       if graph[i][j] == 0:
#         res += 1
#   return res


# def solution(graph):
#   index_of_virus = []
#   for i in range(n):
#     for j in range(m):
#       if graph[i][j] == 2:
#         index_of_virus.append((i, j))

#   cnt = 0 # 세운 벽의 개수
#   result = [] # 안전 영역의 크기 저장
#   copy_graph = graph.copy()
  
#   for i in range(n):
#     for j in range(m):
#       if copy_graph[i][j] == 0:
#         copy_graph[i][j] = 1
#         cnt += 1

#       if cnt == 3:
#         for v in index_of_virus:
#           graph = virus(graph, v)
#         result.append(count_safe_area(graph))
#         cnt -= 1
#         graph[i][j] = 0
        
#   return max(result)

# print(solution(graph))

n, m = map(int, input().split())
data = [] # 초기 맵 리스트
temp = [[0] * m for _ in range(n)] # 벽을 설치한 뒤의 맵 리스트

for _ in range(n):
  data.append(list(map(int, input().split())))

# 4가지 이동 방향에 대한 리스트
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0

# 깊이 우선 탐색(DFS)을 이용해 각 바이러스가 사방으로 퍼지도록 하기
def virus(x, y):
  for i in range(4):
    nx, ny = x + dx[i], y + dy[i]
    # 상하좌우 중에서 바이러스가 퍼질 수 있는 경우
    if nx >= 0 and nx < n and ny >= 0 and ny < m:
      if temp[nx][ny] == 0:
        # 해당 위치에 바이러스 배치하고, 다시 재귀적으로 수행
        temp[nx][ny] = 2
        virus(nx, ny)

# 현재 맵에서 안전 영역의 크기 계산하는 메서드
def get_score():
  score = 0
  for i in range(n):
    for j in range(m):
      if temp[i][j] == 0:
        score += 1
  return score

# 깊이 우선 탐색(DFS)을 이용해 울타리를 설치하면서, 매번 안전 영역의 크기 계산
def dfs(count):
  global result
  # 울타리가 3개 설치된 경우
  if count == 3:
    for i in range(n):
      for j in range(m):
        temp[i][j] = data[i][j]
    # 각 바이러스의 위치에서 전파 진행
    for i in range(n):
      for j in range(m):
        if temp[i][j] == 2:
          virus(i, j)
    # 안전 영역의 최댓값 계산
    result = max(result, get_score())
    return
  # 빈 공간에 울타리 설치
  for i in range(n):
    for j in range(m):
      if data[i][j] == 0:
        data[i][j] = 1
        count += 1
        dfs(count)
        data[i][j] = 0
        count -= 1

dfs(0)
print(result)