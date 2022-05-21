# 표준 라이브러리 : 특정한 프로그래밍 언어에서 자주 사용되는 표준 소스코드를 미리 구현해 놓은 라이브러리

# <내장 함수>
# sum() 함수 : 리스트와 같은 iterable 객체가 입력으로 주어졌을 때, 모든 원소의 합을 반환
# iterable : 반복 가능한 객체 (리스트, 사전, 튜플)
result = sum([1, 2, 3, 4, 5])
print(result)

# min() 함수 : 파라미터가 2개 이상 들어왔을 때 가장 작은 값을 반환
result = min(7, 3, 5, 2)
print(result)

# max() 함수 : 파라미터가 2개 이상 들어왔을 때 가장 큰 값을 반환
result = max(7, 3, 5, 2)
print(result)

# eval() 함수 : 수학 수식이 문자열 형식으로 들어오면 해당 수식을 계산한 결과를 반환
result = eval("(3 + 5) * 7")
print(result)

# sorted() 함수 : iterable 객체가 들어왔을 때, 정렬된 결과를 반환
# key 속성으로 정렬 기준을 명시할 수 있으며, reverse 속성으로 정렬된 결과 리스트를 뒤집을지의 여부를 설정 가능
result = sorted([9, 1, 8, 5, 4])
print(result)
result = sorted([9, 1, 8, 5, 4], reverse = True)
print(result)
# 원소를 튜플의 두 번째 원소(수)를 기준으로 내림차순으로 정렬하고자 할 때
result = sorted([('홍길동', 35), ('이순신', 75), ('아무개', 50)], key = lambda x: x[1], reverse = True)
print(result)

# 리스트와 같은 iterable 객체는 기본적으로 sort() 함수를 내장하고 있음. 이 경우 리스트 객체의 내부 값이 정렬된 값으로 바로 변경됨
data = [9, 1, 8, 5, 4]
data.sort()
print(data)
print('-----')

# <itertools>
# 파이썬에서 반복되는 데이터를 처리하는 기능을 포함하고 있는 라이브러리

# permutations : 리스트 같은 iterable 객체에서 r개의 데이터를 뽑아 일렬로 나열하는 모든 경우(순열)를 계산. 클래스이므로 객체 초기화 이후에는 리스트 자료형으로 변환하여 사용
from itertools import permutations
data = ['A', 'B', 'C'] # 데이터 준비
result = list(permutations(data, 3)) # 모든 순열 구하기
print(result)
print('-----')

# comvinations : 리스트와 같은 iterable 객체에서 r개의 데이터를 뽑아 순서를 고려하지 않고 나열하는 모든 경우(조합)을 계산. 클래스이므로 객체 초기화  이후에는 리스트 자료형으로 변환하여 사용
from itertools import combinations
result = list(combinations(data, 2))
print(result)
print('-----')

# product : permutations와 같이 리스트와 같은 iterable 객체에서 r개의 데이터를 뽑아 일렬로 나열하는 모든 경우(순열) 계산 (원소 중복). product 객체를 초기화할 때는 뽑고자 하는 데이터이 수를 repeat 속성값으로 넣어줌. 클래스이므로 객체 초기화 이후에는 리스트 자료형으로 변환하여 사용
from itertools import product
result = list(product(data, repeat = 2))
print(result)
print('-----')

# combinations_with_replacement : combinations와 같이 리스트와 같은 iterable 객체에서 r개의 데이터를 뽑아 순서를 고려하지 않고 나열하는 모든 경우(조합)을 계산 (원소 중복). 클래스이므로 객체 초기화 이후에는 리스트 자료형으로 변환하여 사용
from itertools import combinations_with_replacement
result = list(combinations_with_replacement(data, 2))
print(result)
print('-----')

# <heapq>
# 힙 기능. 다익스트라 최단 경로 알고리즘을 포함해 다양한 알고리즘에서 우선순위 큐 기능을 구현하고자 할 때 사용.
# 파이썬의 힙은 최소 힙으로 구성되어 있으므로 단순히 원소를 힙에 전부 넣었다가 빼는 것만으로도 시간 복잡도 O(nlogn)에 오름차순 정렬이 완료. 최소 힙 자료구조의 최상단 원소는 항상 가장 작은 원소이기 때문.
# 힙에 원소 삽입 : heapq.heappush()
# 힙에서 원소 꺼낼 때 : heapq.heappop()

# 힙 정렬을 heapq로 구현한 예제
import heapq

def heapsort(iterable):
  h = []
  result = []
  # 모든 원소를 차례대로 힙에 삽입
  for value in iterable:
    heapq.heappush(h, value)
  # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
  for _ in range(len(h)):
    result.append(heapq.heappop(h))
  return result

result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)

# heapq 라이브러리를 이용해 최대 합 구현할 때 : 원소의 부호를 임시로 변경하는 방식 사용 (내림차순 힙 정렬)
def heapsort(iterable):
  h = []
  result = []
  # 모든 원소를 차례대로 힙에 삽입
  for value in iterable:
    heapq.heappush(h, -value)
  # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
  for _ in range(len(h)):
    result.append(-heapq.heappop(h))
  return result

result = heapsort([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
print(result)
print('-----')

# <bisect>
# 이진 탐색 쉽게 구현할 수 있음. 정렬된 배열에서 특정한 원소를 찾아야 할 때 매우 효과적.
# bisect_left(a, x) : 정렬된 순서를 유지하면서 리스트 a에 데이터 x를 삽입할 가장 왼쪽 인덱스를 찾는 메서드
# bisect_right(a, x) : 정렬된 순서를 유지하도록 리스트 a에 데이터 x를 삽입할 가장 오른쪽 인덱스를 찾는 메서드
# 둘다 시간 복잡도 O(logn)
from bisect import bisect_left, bisect_right
a = [1, 2, 4, 4, 8]
x = 4
print(bisect_left(a, x))
print(bisect_right(a, x))
# 두 함수는 정렬된 리스트에서 값이 특정 범위에 속하는 원소의 개수를 구하고자 할 때 효과적으로 사용

# 정렬된 리스트에서 값이 [left_value, right_value]에 속하는 데이터의 개수를 반환하는 예시. (원소의 값을 x라고 할 때, left_value <= x <= right_value인 원소의 개수를 O(logn)으로 빠르게 계산 가능)
def count_by_range(a, left_value, right_value):
  right_index = bisect_right(a, right_value)
  left_index = bisect_left(a, left_value)
  return right_index - left_index

# 리스트 선언
a = [1, 2, 3, 3, 3, 3, 4, 4, 8, 9]

# 값이 4인 데이터 개수 출력
print(count_by_range(a, 4, 4))
# 값이 [-1, 3] 범위에 있는 데이터 개수 출력
print(count_by_range(a, -1, 3))
print('-----')

# <collections>
# deque : 큐 구현. 리스트 자료형과 다르게 인덱싱, 슬라이싱 등의 기능은 사용 못함. 다만, 연속적으로 나열된 데이터의 시작 부분이나 끝 부분에 데이터를 삽입하거나 삭제할 때는 매우 효과적. 스택이나 큐 기능을 모두 포함한다고 볼 수 있기 때문에 스택 혹은 큐 자료구조의 대용으로 사용 가능
# 기본 리스트 자료형의 append(), pop()은 가장 뒤쪽 원소를 기준으로 수행. 따라서 뒤쪽 원소를 처리할 때에는 시간 복잡도가 O(1)이지만 앞쪽 원소는 O(n)임. 그러나 deque는 앞, 뒤쪽 원소 모두 O(1)
# popleft() : 첫 번째 원소 제거
# pop() : 마지막 원소 제거
# appendleft(x) : 첫 번째 인덱스에 원소 x 삽입
# append(x) : 마지막 인덱스에 원소 삽입
# deque를 큐 자료구조(선입선출)로 이용할 때, 원소 삽입은 append(), 원소 삭제는 popleft()
from collections import deque
data = deque([2, 3, 4])
data.appendleft(1)
data.append(5)
print(data)
print(list(data))

# Counter : 등장 횟수 세는 기능. 구체적으로 리스트와 같은 iterable 객체가 주어졌을 때, 해당 객체 내부의 원소가 몇 번씩 등장했는지 알려줌
# 원소별 등장 횟수를 세는 기능 구현
from collections import Counter

counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])

print(counter['blue']) # 'blue'가 등장한 횟수 출력
print(counter['green']) # 'green'이 등장한 횟수 출력
print(dict(counter)) # 사전 자료형으로 변환
print('-----')

# <math>
# 자주 사용되는 수학적인 기능(팩토리얼, 제곱근, 최대공약수 등)을 포함하는 라이브러리

# factorial(x) : x! 값을 반환
import math
print(math.factorial(5)) # 5!

# sqrt(x) : x의 제곱근 반환
print(math.sqrt(7)) # 7의 제곱근 출력

# gcd(a, b) : a와 b의 최대 공약수 반환
print(math.gcd(21, 14))

# pi(파이), 자연상수 e 제공
print(math.pi)
print(math.e)