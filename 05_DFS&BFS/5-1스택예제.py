# 2022-07-03 03:43 ~ 03:47

stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack) # 최하단 원소부터 출력
print(stack[::-1]) # 최상단 원소부터 출력
# 문법 정리
# arr[A:B:C] : index A 부터 index B 까지 C의 간격으로 배열을 만들어라