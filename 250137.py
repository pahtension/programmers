#[PCCP 기출문제] 1번 / 붕대 감기
# https://school.programmers.co.kr/learn/courses/30/lessons/250137

bandage, health, attacks = [5, 1, 5],30,[[2, 10], [9, 15], [10, 5], [11, 5]]

answer = health
attack = 0
for i in attacks:
    time = i[0]-attack-1
    print(time)
    answer += time*bandage[1]+(time//bandage[0])*bandage[2]
    if answer > health:
        answer = health
    attack = i[0]
    print(answer)
    answer -= i[1]
    if answer <=0:
        # return -1
        answer =-1
        break

# return answer
    
print(answer)

def solution(bandage, health, attacks):
    answer = health
    attack = 0
    for i in attacks:
        time = i[0]-attack-1
        answer += time*bandage[1]+(time//bandage[0])*bandage[2]
        if answer > health:
            answer = health
        attack = i[0]
        answer -= i[1]
        if answer <=0:
            return -1
    return answer

