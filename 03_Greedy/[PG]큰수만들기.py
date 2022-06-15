# 2022-06-02 14:21 ~ 16:04
# 리뷰 다음에..

def solution(number, k):
  answer = ''
  removed_cnt = 0 # 제거된 문자열 개수 저장
  reserve_cnt = k + 1 # 최소한 제거하면 안되는 문자열 개수
  i = 0 # 현재 문자열 위치
  while i < len(number):
    if removed_cnt == k:
      answer += number[i:]
      break
    if len(answer) == len(number) - k:
      break
    tmp = number[i:reserve_cnt]
    if '9' in tmp:
      p = tmp.index('9') + i
    else:
      p = tmp.index(max(tmp)) + i
    answer += number[p]
    removed_cnt += (p - i)
    reserve_cnt += 1
    i = p + 1
        
  return answer

number = "654321"
k = 1
print(solution(number, k))