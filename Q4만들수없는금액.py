# 2022-05-30 4:04 ~ 4:23
n = int(input())
coins = list(map(int, input().split()))

max_val = sum(coins)
coins.sort()
val = []

for i in range(len(coins) - 1):
  for j in range(i + 1, len(coins)):
    val.append(sum(coins[i:j+1]))

val.sort()

for i in range(len(val) - 1):
  if val[i] + 1 < val[i+1]:
    res = val[i] + 1
    break

print(res)

# 교재 답안
