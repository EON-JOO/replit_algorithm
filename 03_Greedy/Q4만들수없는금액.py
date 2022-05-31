# 2022-05-30 4:04 ~ 4:23
# 복습 필요!!

n = int(input())
coins = list(map(int, input().split()))

coins.sort()
# val = []

# for i in range(len(coins) - 1):
#   for j in range(i + 1, len(coins)):
#     val.append(sum(coins[i:j+1]))

# val.sort()

# for i in range(len(val) - 1):
#   if val[i] + 1 < val[i+1]:
#     res = val[i] + 1
#     break

# print(res)

# 교재 답안

target = 1
for x in coins:
  # 만들 수 없는 금액을 찾았을 때 반복 종료
  if target < x:
    break
  target += x

# 만들 수 없는 금액 출력
print(target)

# greedy tip
# 1. 최솟값을 구하는 문제는 무조건 for문을 돌릴게 아니라, 오름차순으로 두고 작은 것부터 비교해가면서 풀어야한다.
# 2. 누적합과 화폐단위를 비교해가면서 구해본다. 화폐단위가 누적합보다 클 경우, 그 사이에 갭이 존재한다는 뜻이다.
# 기본적으로 그리디 알고리즘은 현재 상태에서 매번 가장 좋아 보이는 것만을 선택하는 알고리즘 -> 현재 상태를 '1부터 target-1까지의 모든 금액을 만들 수 있는 상태'라고 보고 이때 target인 금액도 만들 수 있는지(현재 확인하는 동전의 단위가 target 이하인지) 체크해서 만들 수 있다면 target의 값을 업데이트(현재 상태를 업데이트)