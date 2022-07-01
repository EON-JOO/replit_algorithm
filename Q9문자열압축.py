# 2022-07-01 02:59 ~ 03:29

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
                if s[i*j:i*j+j] == s[i*j+j:i*j+2*j]:
                    cnt += 1
                    if cnt == 1:
                        tmp += 1
                else:
                    if cnt != 0:
                      tmp += 1
                      cnt = 0
                print("tmp:",tmp,"i:", i)
        answer = min(tmp, answer)
                  
    return answer

print(solution("ababcdcdababcdcd"))