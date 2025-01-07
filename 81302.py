# 거리두기 확인하기 https://school.programmers.co.kr/learn/courses/30/lessons/81302

def solution(places):
    answer = []
    xy = ((1,0),(0,1))

    for i in places:
        breakflug = False
        for row in range(5):
            for col in range(5):
                if i[row][col] == "P":
                    for y,x in xy:
                        dy,dx = row+y, col+x
                        if dy<5 and dx<5:
                            if i[dy][dx] == "P":
                                breakflug = True
                                break
                            elif i[dy][dx] == "O":
                                for yy,xx in xy:
                                    my,mx = dy+yy,dx+xx
                                    if my<5 and mx<5:
                                        if i[my][mx] == "P":
                                            breakflug = True
                                            break
                                if y:
                                    dx-=1
                                    if dx>0:
                                        if i[dy][dx] == "P":
                                            breakflug = True
                                            break
                if breakflug:
                    break
            if breakflug:
                break
        if breakflug:
            answer.append(0)
        else:
            answer.append(1)

    return answer




print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))