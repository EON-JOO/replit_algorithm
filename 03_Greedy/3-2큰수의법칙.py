n, m, k = map(int, input().split())
nums = list(map(int, input().split()))

nums = sorted(nums)
num1 = nums[n-1] # 가장 큰 수
num2 = nums[n-2] # 두 번째로 큰 수

# res, cnt = 0, 0
# for i in range(m):
#   if cnt < k:
#     res += num1
#     cnt += 1
#   else:
#     res += num2
#     cnt = 0

# print(res)

# 이 문제는 M이 10,000 이하이므로 이 방식으로도 문제를 해결할 수 있지만, M의 크기가 100억 이상처럼 커진다면 시간 초과 판정 -> 반복되는 수열 파악으로 단순화

# 가장 큰 수가 더해지는 횟수 계산
cnt = (m // (k + 1)) * k + (m % (k + 1))

res = 0
res = cnt * num1 # 가장 큰 수 더하기
res += (m - cnt) * num2 # 두 번째로 큰 수 더하기

print(res)