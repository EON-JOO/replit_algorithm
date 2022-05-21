# 입력을 위한 전형적인 소스코드
# 데이터의 개수 입력
n = int(input())
# 각 데이터를 공백으로 구분하여 입력
data = list(map(int, input().split()))

data.sort(reverse = True)
print(data)

# 공백을 기준으로 구분하여 적은 수의 데이터 입력
n, m, k = map(int, input().split())

print(n, m, k)

# 입력을 최대한 빠르게 받아야 하는 경우(정렬, 이진 탐색, 최단 경로 문제의 경우 매우 많은 수의 데이터가 연속적으로 입력됨 -> input() 함수는 동작 속도가 느려서 시간 초과의 우려)
# sys.stdin.readline() 함수 이용 : 한 줄씩 입력받기 위해 사용, rstrip() 함수 꼭 호출(readline으로 입력하면 입력 후 엔터가 줄 바굼 기호로 입력되기 때문에, 이 공백 문자를 제거하기 위해 사용)
import sys

# 문자열 입력 받기
data = sys.stdin.readline().rstrip()
print(data)

# 변수 출력 예시
a = 1
b = 2
print(a, b)

# 출력 줄 바꿈 예시
print(a)
print(b)

# 문자열과 수를 함께 출력해야 하는 경우
# 출력시 오류가 발생하는 소스코드 예시
# answer = 7
# print("정답은" + answer + "입니다.")
# -> 문자열 자료형끼리만 더하기 연산이 가능하다는 오류 메시지

# 변수를 문자열로 바꾸어 출력하는 소스코드 예시
answer = 7
print("정답은 " + str(answer) + "입니다.")

# 각 변수를 콤마(,)로 구분하여 출력하는 소스코드 예시
print('정답은', answer, '입니다.')
# 이 경우, 변수의 값 사이에 의도치 않은 공백이 삽입될 수 있음

# f-string 문법
print(f'정답은 {answer}입니다.')