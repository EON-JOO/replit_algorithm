# 프로그래머스 Greedy 1단계 체육복
# 2022-05-31 16:13 ~ 16:30

# 내 답안
# def solution(n, lost, reserve):
#   answer = 0

#   # 전체 학생의 체육복 개수를 담은 리스트 생성
#   data = [1] * n
#   for x in lost:
#     data[x - 1] -= 1
#   for y in reserve:
#     data[y - 1] += 1
    
#   for i in range(n):
#     if data[i] == 0: # 체육복을 도난당한 경우
#       if i == 0: # 맨 앞사람이면?
#         if data[1] == 2: # 뒷사람이 여벌이 있는 경우
#           data[1] -= 1
#           data[i] += 1
#           answer += 1
#         else: # 뒷사람 여벌 없는 경우
#           continue
#       elif i == n - 1: # 맨 뒷사람이면?
#         if data[n - 2] == 2: # 앞사람이 여별이 있는 경우
#           data[n - 2] -= 1
#           data[i] += 1
#           answer += 1
#         else: # 앞사람 여벌 없는 경우
#           continue
#       else: # 맨앞뒤가 아니면
#         if data[i - 1] == 2: # 앞사람이 여벌이 있는 경우
#           data[i - 1] -= 1
#           data[i] += 1
#           answer += 1
#         elif data[i + 1] == 2: # 뒷사람이 여벌이 있는 경우
#           data[i + 1] -= 1
#           data[i] += 1
#           answer += 1
#         else: # 앞뒷사람 둘다 여벌이 없는 경우
#           continue
#     else: # 체육복 도난 안 당한 경우
#       answer += 1                  
    
#   return answer

# review : 일단 중복되는 경우를 생각하지 못하고 if문으로 조져버린 것.. 기준을 도난당한 학생으로 잡았는데, 여벌 체육복이 있는 학생으로 잡아서 풀면 훨씬 간단.

# 모범 답안
# 여벌 체육복을 가져온 학생이 체육복을 도난당했을 경우 -> 집합 set을 이용해서 중복을 삭제
# 여벌 체육복이 있는 학생을 기준으로 앞뒤 학생이 도난당했는지 확인해서 도난당했으면 빌려주고 lost에서 제외
# 전체 학생 수에서 lost에 남아있는 학생 수(빌릴 수 없는 학생)를 빼면 답

def solution(n, lost, reserve):
  _reserve = list(set(reserve) - set(lost))
  _lost = list(set(lost) - set(reserve))

  for r in _reserve:
    front = r - 1
    back = r + 1
    if front in _lost:
      _lost.remove(front)
    elif back in _lost:
      _lost.remove(back)
      
  return n - len(_lost)

n = int(input())
lost = list(map(int, input().split()))
reserve = list(map(int, input().split()))
print(solution(n, lost, reserve))