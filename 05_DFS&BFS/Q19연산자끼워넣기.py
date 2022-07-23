# 2022-07-21 04:05 ~ 04:37

# 교재 답안

n = int(input())
# 연산을 수행하고자 하는 수 리스트
data = list(map(int, input().split()))
# 더하기, 빼기, 곱하기, 나누기 연산자 개수
add, sub, mul, div = map(int, input().split())

# 최솟값, 최댓값 초기화
min_val = 1e9
max_val = -1e9

l = []

# DFS 메서드
def dfs(i, now):
  global n, min_val, max_val, add, sub, mul, div
  # 모든 연산자를 다 사용한 경우, 최솟값과 최댓값 업데이트
  if i == n:
    # print("3개 다고름 ~ ", l)
    min_val = min(min_val, now)
    max_val = max(max_val, now)
  else:
    # 각 연산자에 대하여 재귀적으로 수행
    if add > 0:
      add -= 1
      # l.append('+')
      dfs(i + 1, now + data[i])
      # print(l)
      # l.pop()
      add += 1
    if sub > 0:
      sub -= 1
      # l.append('-')
      dfs(i + 1, now - data[i])
      # print(l)
      # l.pop()
      sub += 1
    if mul > 0:
      mul -= 1
      # l.append('*')
      dfs(i + 1, now * data[i])
      # print(l)
      # l.pop()
      mul += 1
    if div > 0:
      div -= 1
      # l.append('/')
      dfs(i + 1, int(now / data[i]))
      # print(l)
      # l.pop()
      div += 1

dfs(1, data[0])

print(max_val)
print(min_val)