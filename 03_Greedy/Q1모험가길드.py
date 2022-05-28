# 2022-05-28 19:30 ~ 19:48
n = int(input())
horror_rate = list(map(int, input().split()))

horror_rate.sort()

cnt, res = 0, 0
# max_rate = 0
# for num in horror_rate:
#   max_rate = num # 현재 공포도 저장
#   cnt += 1 # 그룹에 포함된 모험가 수 count
#   # 그룹에 포함된 모험가 수와 현재 공포도 비교
#   if cnt == max_rate: --> 크거나 같을 때로 바꿔야 함
#     res += 1
#     cnt = 0

# 교재 답안
for i in horror_rate: # 공포도를 낮은 것부터 하나씩 확인하며
  cnt += 1 # 현재 그룹에 해당 모험가를 포함시키기
  if cnt >= i: # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹 결성
    res += 1 # 총 그룹수 증가
    cnt = 0 # 현재 그룹에 포함된 모험가의 수 초기화

print(res)

# 왜 cnt >= i 인지? 최소한의 모험가의 수만 포함해서 최대한 많은 그룹을 결성하는 것이기 때문에 공포도 이상으로 모험가를 넣는 방식으로 알고리즘이 돌아가지 않아서 굳이 >를 넣어야 하나라는 궁금증이 있음