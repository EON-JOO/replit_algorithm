# 2022-05-31 01:57 ~ 02:50
# 채점 결과
# 정확성: 10.7
# 효율성: 0.0
# 합계: 10.7 / 100.0
# 우선순위 큐 -> 9장 다익스트라 알고리즘 학습 후 다시 풀기

def solution(food_times, k):
  answer = 0
  number_of_food = len(food_times) # 음식 개수
  circle = k // number_of_food # k초 전에 회전판이 몇 바퀴 돌았는지
  extra_time = k % number_of_food # 회전판이 전체 음식을 돌고 남은 시간
    
  # k초 동안 회전판이 돈 만큼(음식을 먹은 만큼) 시간 빼기
  for i in range(number_of_food):
    food_times[i] -= (circle + 1)
        
  x = 0
  if extra_time == 0: # 이미 회전판을 k번 돌린 경우
    for j in range(number_of_food):
      if food_times[j] > 0:
        answer = j + 1
        return answer
    return -1
  else: # 더 돌려야 할 경우, k초 후에 먹어야 할 음식 번호 찾기
    for i in range(number_of_food):
      if food_times[i] >= 0:
        extra_time -= 1
      if extra_time == 0:
        x = i # x는 확인해야 할 음식 번호
        break
    
  start = x
  x += 1
  while True:
    if x == number_of_food:
      x = 0
      continue
    else:
      if food_times[x] > 0:
        answer = x + 1
        break
      else:
        if x == start - 1:
          answer = -1
          break
        x += 1
                    
  return answer

food_times = list(map(int, input().split()))
k = int(input())
print(solution(food_times, k))