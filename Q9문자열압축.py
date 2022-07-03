# 2022-07-01 02:59 ~ 03:29
# 2022-07-03 03:08 ~ 3:18

def solution(s):
    tmp = 0
    len_s = len(s)
    answer = len_s
    print(len_s)
    
    for i in range(1, len_s // 2):
        if len_s % i == 0: # s를 i개로 자를 수 있을 때
            cnt = 0 # 중복된 숫자 갯수
            tmp += 1
            for j in range(len_s // i):
                # 다음 i개의 숫자와 같을 때
                if s[i*j:i*j+i] == s[i*j+i:i*j+2*i]:
                    cnt += 1
                    if cnt == 1:
                        tmp += 1
                # 다음 j개의 숫자와 같지 않을 때
                else:
                    tmp += 1
                    if cnt != 0:
                      cnt = 0
                print("tmp:",tmp,"i:", i)
        answer = min(tmp, answer)
                  
    return answer

print(solution("ababcdcdababcdcd"))

# 실패... 복습..!!
# 입력으로 주어지는 문자열의 길이가 1000 이하 -> 가능한 모든 경우의 수를 탐색하는 완전 탐색을 수행할 수 있음
# 길이가 n인 문자열이 입력되었다면 1부터 n/2까지의 모든 수를 단위로 하여 문자열을 압축하는 방법을 모두 확인하고 가장 짧게 압축되는 길이를 출력
# => 아이디어는 맞았으나 구현 실패

# 교재 답안
# def solution(s):
#   answer = len(s)
#   # 1개의 단위(step)부터 압축 단위를 늘려가며 확인
#   for step in range(1, len(s) // 2 + 1):
#     compressed = ""
#     prev = s[0:step]
#     count = 1
#     # 단위(step) 크기만큼 증가시키며 이전 문자열과 비교
#     for j in range(step, len(s), step):
#       # 이전 상태와 동일하다면 압축 횟수(count) 증가
#       if prev == s[j:j + step]:
#         count += 1
#       # 다른 문자열이 나왔다면(더 이상 압축하지 못하는 경우라면)
#       else:
#         compressed += str(count) + prev if count >= 2 else prev
#         prev = s[j:j + step] # 다시 상태 초기화
#         count = 1
#     # 남아 있는 문자열에 대해서 처리
#     compressed += str(count) + prev if count >= 2 else prev
#     # 만들어지는 압축 문자열이 가장 짧은 것이 정답
#     answer = min(answer, len(compressed))
#   return answer