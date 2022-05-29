# 2022-05-29 23:26 ~ 23:30

s = list(map(int, input()))
res = s[0]

for i in range(1, len(s)):
  # if res == 0 or s[i] == 0:
  #   res += s[i]
  # elif res == 1 or s[i] == 1:
  #   res += s[i]
  # 좀더 간략화 할 수 있음
  if res <= 1 or s[i] <= 1:
    res += s[i]
  else:
    res *= s[i]

print(res)

# data = input() 그냥 이렇게 받아서
# num = int(data[0]) 이렇게 해도 됨