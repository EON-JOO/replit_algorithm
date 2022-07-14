# 2022-07-14 04:15 ~ 04:36
# dfs/bfs 실전 문제 풀이에 대한 감을 못 잡아서 답안 보고 공부 -> 복습 필요!!

from collections import deque

n, m = map(int, input().split())
graph = []
for _ in range(n):
  graph.append(list(map(int, input())))

# 이동할 네 방향 정의 (상하좌우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 소스코드 구현
def bfs(x, y):
  # 큐(Queue) 구현을 위한 deque 라이브러리 사용
  queue = deque()
  queue.append((x, y))
  # 큐가 빌 때까지 반복
  while queue:
    x, y = queue.popleft()
    # 현재 위치에서 네 방향으로의 위치 확인
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      # 미로 찾기 공간을 벗어난 경우 무시
      if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue
      # 괴물이 있을 경우 무시
      if graph[nx][ny] == 0:
        continue
      # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
      if graph[nx][ny] == 1:
        graph[nx][ny] = graph[x][y] + 1
        queue.append((nx, ny))
  # 가장 오른쪽 아래까지의 최단 거리 반환
  return graph[n - 1][m - 1]

print(bfs(0, 0))

print(graph)

# 최단 거리이므로 bfs 사용, bfs는 시작 지점에서 가가운 노드부터 차례대로 그래프의 모든 노드를 탐색하기 때문 -> (1, 1) 지점에서부터 bfs를 수행하여 모든 노드의 값을 거리 정보로 넣으면 됨. 특정한 노드를 방문하면 그 이전 노드의 거리에 1을 더한 값을 리스트에 넣음
# 참고로 소스코드 상에서, 첫 번째 시작 위치는 다시 방문할 수 있도록 되어 첫 번째 시작 위치에 해당하는 값이 3으로 변경될 여지가 있음. 그러나 본 문제에서는 단순히 가장 오른쪽 아래 위치로 이동하는 것을 요구하고 있기 때문에 본 소스코드는 정상적으로 답을 도출하는 간결한 정답 코드임