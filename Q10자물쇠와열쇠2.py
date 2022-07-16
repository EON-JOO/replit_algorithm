# 2022-07-16 03:19 ~ 03:35

def rotate_key(a): # 90도 회전
  m = len(a)
  res = [[0] * m for _ in range(m)]
    
  for i in range(m):
    for j in range(m):
      res[i][j] = a[j][m - i - 1]
  return res

def check(new_lock): # lock이 모두 1인지 확인
  n = len(new_lock) // 3
    
  for i in range(n, n * 2):
    for j in range(n, n * 2):
      if new_lock[i][j] != 1:
        return False
  return True

def solution(key, lock):
  n = len(lock)
  m = len(key)
    
  new_lock = [[0] * (n * 3) for _ in range(n * 3)]
    
  for i in range(n):
    for j in range(n):
      new_lock[n + i][n + j] = lock[i][j]
    
  for _ in range(4): # 4 방향으로 key 회전
    key = rotate_key(key)
        
    for x in range(n * 2):
      for y in range(n * 2):
        # key와 lock을 더한다
        for i in range(m):
          for j in range(m):
            new_lock[x + i][y + j] += key[i][j]
                
        if check(new_lock):
          return True
                
        # key와 lock을 뺀다
        for i in range(m):
          for j in range(m):
            new_lock[x + i][y + j] -= key[i][j]
                        
    return False