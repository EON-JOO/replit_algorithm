# 2022-07-20 03:33 ~ 03:53
# 굿 ~

p = input()

def separate(w): # u와 v로 분리
  cnt = 0
  for i in range(len(w)):
    if w[i] == '(':
      cnt += 1
    else:
      cnt -= 1
    if cnt == 0:
      return i


def check(u): # 올바른 괄호 문자열인지 확인
  cnt = 0
  for i in range(len(u)):
    if u[i] == '(':
      cnt += 1
    else:
      if cnt == 0:
        return False
      cnt -= 1
  return True


def dfs(p):
  if len(p) == 0:
    return ""

  i = separate(p)
  u = p[:i + 1]
  v = p[i + 1:]

  if check(u) == True:
    return u + dfs(v)
  else:
    tmp = '(' + dfs(v) + ')'
    u = u[1:-1]
    reverse_u = ""
    for ele in u:
      if ele == '(':
        reverse_u += ')'
      else:
        reverse_u += '('
    return tmp + reverse_u


print(dfs(p))