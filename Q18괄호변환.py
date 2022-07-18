# 2022-07-18 03:36 ~ 04:06

# 함수의 구성(균형 잡힌 괄호 인덱스 반환, 올바른 괄호인지 확인)은 맞았으나 올바른 괄호인지 확인하는 함수 오답. 재귀적인 부분 구현 못함.

# 답안 보고 2차 시도
def count_of_bracket(p):
  right, left = 0, 0
  for i in range(len(p)):
    if p[i] == '(':
      right += 1
    else:
      left += 1
    if right == left:
      return i

def check(u):
  cnt = 0
  for i in range(len(u)):
    if u[i] == '(':
      cnt += 1
    else:
      if cnt == 0:
        return False
      cnt -= 1
  return True

def solution(p):
  answer = ''
  length = len(p)
  if length == 0:
    return ''

  x = count_of_bracket(p)
  u = p[:x+1]
  v = p[x+1:]
  if check(u) == True: # '올바른 괄호 문자열'이면
    answer = u + solution(v)
  else: # '올바른 괄호 문자열'이 아니면
    answer = '(' + solution(v) + ')'
    u = u[1:-1]
    for ele in u:
      if ele == '(':
        answer += ')'
      else:
        answer += '('
  
  return answer

arr = input()
print(solution(arr))

# 답안 안본 1차 시도
# def count_of_bracket(p):
#   right, left = 0, 0
#   for i in range(n):
#     if p[i] == '(':
#       right += 1
#     else:
#       left += 1
#     if right == left:
#       return i

# def check(u):
#   right, left = 0, 0
#   for i in range(n):
#     if p[i] == '(':
#       right += 1
#     else:
#       left += 1
#   if right == left:
#     return True
#   else:
#     return False

# def solution(p):
#   answer = ''
#   length = len(p)
#   if length == 0:
#     return ''
    
#   w = p
#   while w:
#     x = count_of_bracket(w)
#     u = w[:i+1]
#     v = w[i+1:]
#     if check(u) == True: # '올바른 괄호 문자열'이면
#       answer += u
#       w = v
#     else: # '올바른 괄호 문자열'이 아니면
#       tmp = '(' + v에 대해 재귀 수행 결과 + ')'
#       u = u[1:-1]
#       for ele in u:
#         if ele == '(':
#           tmp += ')'
#         else:
#           tmp += '('
#       answer += tmp
#   return answer