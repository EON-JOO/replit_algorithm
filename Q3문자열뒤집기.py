# 2022-05-29 23:35 ~ 23:48

s = list(map(int, input()))

ss = []
ss.append(s[0])
for i in range(1, len(s)):
  if ss[-1] != s[i]:
    ss.append(s[i])

cnt_0 = ss.count(0)
cnt_1 = ss.count(1)
print(min(cnt_0, cnt_1))