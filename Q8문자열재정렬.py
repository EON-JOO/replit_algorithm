# 2022-06-29 03:41 ~ 03:50

s = input()
res = 0
new_s = ''

for elem in s:
  if elem.isdigit():
    res += int(elem)
  elif elem.isalpha():
    new_s += elem

new_s = ''.join(s for s in sorted(new_s))

print(new_s + str(res))

# 문법 정리
# a.isdigit() : 숫자인지 확인
# a.isalpha() : 알파벳인지 확인

# a.sort() : 리스트에 대한 함수 (본체의 리스트 정렬)
# sorted(a) : 문자열도 가능 -> 리스트로 반환(본체 리스트 보존, 정렬한 새로운 리스트 반환)

# 리스트 -> 문자열 변환
# str_list = ['This', 'is', 'a', 'python tutorial']
# result = ' '.join(s for s in str_list)
# print(result) -> Output: This is a python tutorial

# 숫자 섞인 리스트 -> 문자열 변환
# str_list = ['There', 'is', 4, "items"]
# result = ' '.join(str(s) for s in str_list)
# print(result) -> Ouput: There is 4 items

# 숫자 섞인 리스트 -> 문자열 변환 (map 이용)
# str_list = ['There', 'is', 4, "items"]
# result = ' '.join(map(str, str_list))
# print(result) -> Ouput: There is 4 items

# 틀린 부분 : 숫자가 존재하지 않는 경우에는 0이 붙게 되므로 숫자가 존재하는지 확인하는 처리도 해줘야 함
# 교재 답안
# data = input()
# result = []
# value = 0

# 문자를 하나씩 확인하며
# for x in data:
#   # 알파벳인 경우 결과 리스트에 삽입
#   if x.isalpha():
#     result.append(x)
#   # 숫자는 따로 더하기
#   else:
#     value += int(x)

# 알파벳을 오름차순으로 정렬
# result.sort()

# 숫자가 하나라도 존재하는 경우 가장 뒤에 삽입
# if value != 0:
#   result.append(str(value))

# 최종 결과 출력(리스트를 문자열로 변환하여 출력)
# print(''.join(result))