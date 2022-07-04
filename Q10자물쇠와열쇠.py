# 2022-07-04 01:41 ~ 02:55

# def solution(key, lock):
#   m = len(key[0])
#   n = len(lock[0])
#   answer = True
#   new_lock = [[0] * (m+n+1) for _ in range(m+n+1)]
    
#   for i in range(m):
#     for j in range(m):
#       new_lock[i+2][j+2] = lock[i][j]
    
#   for i in range(m+n-1):
#     for j in range(m+n-1):
#       tmp = new_lock.copy()
#       crop_tmp = [row[j:j+m] for row in tmp[i:i+m]]
#       key_lock = [crop_tmp[x][y] + key[x][y] for x in range(m) for y in range(m)]

#       if 2 in key_lock:
#         answer = False
#         return answer
#       if 

#   return answer

# 실패... 복습..!
# 문제에서 제시한 자물쇠와 열쇠의 크기는 20*20보다 작으므로 크기가 20*20인 2차원 리스트에 있는 모든 원소에 접근할 때는 400만큼의 연산이 필요
# 파이썬의 경우 일반적인 코딩 테스트 채점 환경에서 1초에 2000만에서 1억 정도의 연산을 처리할 수 있으므로 "완전 탐색"을 이용해서 열쇠를 이동이나 회전시켜서 자물쇠에 끼워보는 작업을 전부 시도해보는 접근 방법을 이용할 수 있음
# 가장 먼저 자물쇠를 크기가 3배인 새로운 리스트로 만들어 중앙 부분으로 옮김. 열쇠 배열을 왼쪽 위부터 시작해서 한 칸씩 이동하는 방식으로 차례대로 자물쇠의 모든 홈을 채울 수 있는지 확인 -> 자물쇠 리스트에 열쇠 리스트의 값을 더한 뒤에, 더한 값을 확인했을 때 자물쇠 부분의 모든 값이 정확히 1인지 확인

# 교재 답안

# 2차원 리스트 90도 회전
def rotate_a_matrix_by_90_degree(a):
  n = len(a) # 행 길이 계산
  m = len(a[0]) # 열 길이 계산
  result = [[0] * m for _ in range(m)] # 결과 리스트
  for i in range(n):
    for j in range(m):
      result[j][n - i - 1] = a[i][j]
  return result

# 자물쇠의 중간 부분이 모두 1인지 확인
def check(new_lock):
  lock_length = len(new_lock) // 3
  for i in range(lock_length, lock_length * 2):
    for j in range(lock_length, lock_length * 2):
      if new_lock[i][j] != 1:
        return False
  return True

def solution(key, lock):
  n = len(lock)
  m = len(key)
  # 자물쇠의 크기를 기존의 3배로 변환
  new_lock = [[0] * (n * 3) for _ in range(n * 3)]
  # 새로운 자물쇠의 중앙 부분에 기존의 자물쇠 넣기
  for i in range(n):
    for j in range(n):
      new_lock[i + n][j + n] = lock[i][j]

  # 4가지 방향에 대해서 확인
  for rotation in range(4):
    key = rotate_a_matrix_by_90_degree(key) # 열쇠 회전
    for x in range(n * 2):
      for y in range(n * 2):
        # 자물쇠에 열쇠 끼워 넣기
        for i in range(m):
          for j in range(m):
            new_lock[x + i][y + j] += key[i][j]
        # 새로운 자물쇠에 열쇠가 정확히 들어맞는지 검사
        if check(new_lock) == True:
          return True
        # 자물쇠에서 열쇠 다시 빼기
        for i in range(m):
          for j in range(m):
            new_lock[x + i][y + j] -= key[i][j]
  return False

key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(key, lock))

# lock 리스트를 padding해서 key 리스트를 더하는 것까지는 접근 방식이 맞았으나, 90도 회전 구현을 못했고 전반적으로 리스트 다루는 구현이 무족함