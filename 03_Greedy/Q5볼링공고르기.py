# 2022-05-31 00:53 ~ 01:11
# 복습 필요!!

n, m = tuple(map(int, input().split()))
data = list(map(int, input().split()))

# data.sort()
# res = n * (n - 1) // 2

# for i in range(len(data) - 1):
#   for j in range(i + 1, len(data)):
#     if data[i] == data[j]:
#       res -= 1

# print(res)

# 교재 답안

# 1부터 10까지의 무게를 담을 수 있는 리스트
arr = [0] * 11

for x in data: # 각 무게에 해당하는 볼링공 개수 카운트
  arr[x] += 1

res = 0
# 1부터 m까지의 각 무게에 대하여 처리
for i in range(1, m + 1):
  n -= arr[i] # 무게가 i인 볼링공의 개수(A가 선택할 수 있는 개수) 제외
  res += arr[i] * n # B가 선택하는 경우의 수와 곱하기

print(res)