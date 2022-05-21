# <while문>
# 1부터 9까지 각 정수의 합을 계산하는 코드
i = 1
result = 0

# i가 9보다 작거나 같을 때 아래 코드를 반복적으로 실행
while i <= 9:
  result += i
  i += 1

print(result)

# 1부터 9까지의 수 중에서 홀수만 더하는 코드
i = 1
result = 0

while i <= 9:
  if i % 2 == 1:
    result += i
  i += 1

print(result)
print("----")

# <for문>
# 1부터 9까지의 정수의 합을 구하는 코드
result = 0

# i는 1부터 9까지의 모든 값을 순회
for i in range(1, 10):
  result += i
print(result)
print("----")

# 리스트나 튜플 데이터의 모든 원소를 첫 번째 인덱스부터 방문해야 할 때
scores = [90, 85, 77, 65, 97]

for i in range(5):
  if scores[i] >= 80:
    print(i + 1, "번 학생은 합격입니다.")
print("----")

# 블랙리스트에 해당 번호가 포함된 경우, 해당 학생은 무시하고 다시 다음 번호부터 처리하도록 할 때
cheating_list = {2, 4}

for i in range(5):
  if i + 1 in cheating_list:
    continue
  else:
    if scores[i] >= 80:
      print(i + 1, "번 학생은 합격입니다.")
print("----")

# 구구단 2단부터 9단까지의 모든 결과 출력하는 코드
for i in range(2, 10):
  for j in range(1, 10):
    print(i, "X", j, "=", i * j)
  print()