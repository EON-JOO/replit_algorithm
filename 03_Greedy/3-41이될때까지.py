n, k = tuple(map(int, input().split()))

# cnt = 0
# while n != 1:
#   if n % k == 0:
#     n /= k
#   else:
#     n -= 1
#   cnt += 1

# 문제에서는 N의 범위가 10만 이하이므로, 위처럼 일일이 1씩 빼도 문제를 해결할 수 있으나, N이 100억 이상의 큰 수가 되는 경우를 가정했을 때에도 빠르게 동작하려면 N이 K의 배수가 되도록 효율적으로 한 번에 빼는 방식으로 작성

cnt = 0
while (n >= k): # 더 이상 나눌 수 없을 때까지
  if n % k != 0: # n가 k으로 나눠 떨어지지 않으면
    cnt += n % k
    n -= (n % k)
  else: # 나눠 떨어지면
    n //= k
    cnt += 1

# 교재 답안
# while True:
#   # (n == k로 나눠떨어지는 수)가 될 때까지 1씩 빼기
#   target = (n // k) * k
#   cnt += (n - target)
#   n = target
#   # n이 k보다 작을 때(더 이상 나눌 수 없을 때) 반복문 탈출
#   if n < k:
#     break
#   cnt += 1
#   n //= k

cnt += (n - 1)

print(cnt)