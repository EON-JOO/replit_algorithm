# 더하기 기능을 제공하는 함수
def add(a, b):
  return a + b

print(add(3, 7))

# return문 없이
def add(a, b):
  print("함수의 결과 :", a + b)

add(3, 7)

# 함수를 호출하는 과정에서 인자를 넘겨줄 때, 파라미터의 변수를 직접 지정해서 값을 넣을 수 있음
# 이 경우 매개변수의 순서가 달라도 상관없음
def add(a, b):
  print('함수의 결과 :', a + b)

add(b = 7, a = 3)

# 함수 안에서 함수 밖의 변수 데이터를 변경해야 하는 경우 -> 함수에서 global 키워드를 사용
# 해당 함수에서는 지역 변수를 만들지 않고, 함수 바깥에 선언된 변수를 바로 참조
a = 0

def func():
  global a
  a += 1

for i in range(10):
  func()

print(a)

# 람다 표현식 : 특정한 기능을 수행하는 함수를 한 줄에 작성할 수 있음. 파이썬의 정렬 라이브러리를 사용할 때, 정렬 기준(Key)를 설정할 때에도 자주 사용
# lambda 파라미터 : 함수식
# 간단한 함수 만들 때 유용
def add(a, b):
  return a + b

# 일반적인 add() 메서드 사용
print(add(3, 7)) 
# 람다 표현식으로 구현한 add() 메서드
print((lambda a, b: a + b)(3, 7))