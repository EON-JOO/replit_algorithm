# 2022-05-31 17:21 ~ 18:04
# 채점 결과
# 정확성: 63.0
# 합계: 63.0 / 100.0
# 일단 그리디로 안 풀었고, 테스트케이스 추가되어서 그리디로 안되고 완전탐색(Brute Force)으로 풀림 -> 추후 다시 풀이 시도
# https://velog.io/@jqdjhy/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%A1%B0%EC%9D%B4%EC%8A%A4%ED%8B%B1-Greedy

def solution(name):
    answer = 0
    len_name = len(name)
    
    name_ = []
    for ele in name: # name을 숫자로 바꾼 리스트 (A : 1)
        name_.append(ord(ele) - 64)
    
    # A가 아닌 위치 저장
    not_A = []
    for i in range(len(name_)):
        if name_[i] != 1:
            not_A.append(i)
    
    # 커서 이동 최소 횟수 계산
    if not not_A: # 모두 A일 때
        answer = 0
        return answer
    elif not_A == [0]: # 첫 번째 알파벳만 A가 아닐 때
        answer = 0
    elif len(not_A) == 1: # 첫 번째가 아닌 알파벳 하나만 A가 아닐 때
        answer = min(not_A[0], len_name - not_A[0])
    else: # 그 외
        answer = min(not_A[-1], len_name - not_A[1])
    
    # 각 자리의 알파벳 조정 횟수 계산
    for x in not_A:
        if name_[x] <= 14: # 위로 이동(다음 알파벳)하는 것이 최소일 때
            answer += name_[x] - 1
        else: # 아래로 이동(이전 알파벳)하는 것이 최소일 때
            answer += (26 - name_[x] + 1)
    
    return answer