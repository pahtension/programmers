# 광물 캐기 https://school.programmers.co.kr/learn/courses/30/lessons/172927

def solution(picks, minerals):
    answer = 0
    l = []
    l2 = []
    for i in minerals:
        if len(l2)==5:
            l.append(l2)
            l2 = []
        l2.append(25 if i=="diamond" else 5 if i=="iron" else 1)
    if len(l2)!=0:
        l.append(l2)
    l2 = [sum(i) for i in l[:sum(picks)]]
    for i in sorted(l2,reverse=True):
        for j in l.pop(l2.index(i)):
            if picks[0]:
                answer +=1
            elif picks[1]:
                answer += 5 if j ==25 else 1
            elif picks[2]:
                answer += j

        picks[0 if picks[0] else 1 if picks[1] else 2] -=1
        l2.remove(i)
        if not l:
            break

    return answer

