# 어떤 변수의 값이 10 이상일 때만, 변수의 값을 출력
x = 15
if x >= 10:
  print(x)
print("----")

# 성적 구간에 따른 학점 정보 출력
score = 85
if score >= 90:
  print("학점 : A")
elif score >= 80:
  print("학점 : B")
elif score >= 70:
  print("학점 : C")
else:
  print("학점 : F")
print("----")

# 조건문을 작성할 때는 코드의 블록을 들여쓰기로 설정
if score >= 70:
  print("성적인 70점 이상입니다.")
  if score >= 90:
    print("우수한 성적입니다.")
else:
  print("성적이 70점 미만입니다.")
  print("조금 더 분발하세요.")
print("프로그램을 종료합니다.")
print("----")

# <비교 연산자>
# X == Y : X와 Y가 서로 같을 때 True
# X != Y : X와 Y가 서로 다를 때 True
# X > Y, X < Y, X >= Y, X <= Y

# <논리 연산자>
# X and Y : X와 Y가 모두 True일 때 True
# X or Y : X와 Y 중에 하나만 True여도 True
# not X : X가 False일 때 True

# <파이썬의 기타 연산자>
# X in 리스트 : 리스트 안에 X가 들어가 있을 때 True
# X not in 문자열 : 문자열 안에 X가 들어가 있지 않을 때 True

# 조건문의 값이 True라고 해도, 아무것도 처리하고 싶지 않을 때 pass문 사용
if score >= 80:
  pass
else:
  print("성적이 80점 미만입니다.")
print("프로그램을 종료합니다.")
print("----")

# 조건문에서 실행될 소스코드가 한 줄일 경우, 굳이 줄 바꿈을 하지 않고도 간략하게 표현 가능
if score >= 80: result = "Success"
else: result = "Fail"
print(result)
print("----")

# 조건부 표현식
result = "Success" if score >= 80 else "Fail"
print(result)
print("----")
# 조건부 표현식은 리스트에 있는 원소의 값을 변경해서, 또 다른 리스트를 만들고자 할 때 매우 간결하게 사용 가능
# 예를 들어 특정한 원소의 값만을 없애는 경우
# 일반적인 형태의 조건문
a = [1, 2, 3, 4, 5, 5, 5]
remove_set = {3, 5}

result = []
for i in a:
  if i not in remove_set:
    result.append(i)

print(result)

# 조건부 표현식 사용
result = [i for i in a if i not in remove_set]
print(result)