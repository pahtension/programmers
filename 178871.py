# 달리기 경주  https://school.programmers.co.kr/learn/courses/30/lessons/178871

def solution(players, callings):
    d = {}
    for i,v in enumerate(players):
        d.update({v:i})

    for i in callings:
        id = d[i]
        players[id],players[id-1] = zp,p = players[id-1],players[id]
        
        d.update({p:id-1})
        d.update({zp:id})

    return players
