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

# 모든 숫자를 전부 같게 만드는 것이 목적 -> 전부 0으로 바꾸는 경우와 전부 1로 바꾸는 경우 중에서 더 작은 횟수를 가지는 경우를 계산

# 교재 답안
# data = input()
# count0 = 0 # 전부 0으로 바꾸는 경우
# count1 = 0 # 전부 1로 바꾸는 경우

# # 첫 번째 원소에 대해서 처리
# if data[0] == '0':
#   count1 += 1
# else:
#   count0 += 1

# # 두 번째 원소부터 모든 원소를 확인하며
# for i in range(len(data) - 1):
#   if data[i] != data[i + 1]:
#     # 다음 수에서 1로 바뀌는 경우
#     if data[i + 1] == '1':
#       count0 += 1
#     # 다음 수에서 0을 바뀌는 경우
#     else:
#       count1 += 1

# print(min(count0, count1))