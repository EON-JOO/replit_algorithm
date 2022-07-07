# 2022-07-07 04:04 ~ 04:28
# dfs/bfs 실전 문제 풀이에 대한 감을 못 잡아서 답안 보고 공부 -> 복습 필요!!

# n, m을 공백으로 구분하여 입력 받기
n, m = map(int, input().split())

# 2차원 리스트의 맵 정보 입력 받기
graph = []
for i in range(n):
  graph.append(list(map(int, input())))

# DFS로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def dfs(x, y):
  # 주어진 범위를 벗어나는 경우에는 즉시 종료
  if x < 0 or x >= n or y < 0 or y >= m:
    return False
  # 현재 노드를 아직 방문하지 않았다면
  if graph[x][y] == 0:
    # 해당 노드 방문 처리
    graph[x][y] = 1
    # 상, 하, 좌, 우의 위치도 모두 재귀적으로 호출
    dfs(x - 1, y)
    dfs(x, y - 1)
    dfs(x + 1, y)
    dfs(x, y + 1)
    return True
  return False

# 모든 노드(위치)에 대해 음료수 채우기
result = 0
for i in range(n):
  for j in range(m):
    # 현재 위치에서 DFS 수행
    if dfs(i, j) == True:
      result += 1

print(result)

# dfs 메서드는 현재 노드를 방문하지 않았으면 True를 return함과 동시에 상하좌우 노드도 dfs 메서드를 호출해서 방문하지 않은 0이 있다면 1로 방문 처리한다. 즉, 연결되어 있는 노드들이 모두 방문처리가 되고, 해당 위치에서 첫 방문 처리가 아니면 False가 return되어 True일 때만 count하면 연결된 노드들의 갯수가 나온다.