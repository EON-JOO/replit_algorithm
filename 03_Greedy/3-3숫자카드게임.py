n, m = tuple(map(int, input().split()))
nums = [list(map(int, input().split())) for _ in range(n)]

# max_list = []
# for row in nums:
#   max_list.append(min(row))

# res = max(max_list)

res = 0
for row in nums:
  tmp = min(row)
  res = max(res, tmp)

print(res)