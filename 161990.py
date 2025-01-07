# 바탕화면 정리  https://school.programmers.co.kr/learn/courses/30/lessons/161990

def solution(wallpaper):
    answer = [ 0, 0,      0, 0 ]
    #      min y  x   max y  x

    xlen = len(wallpaper[0])
    flag = False
    for y in range(len(wallpaper)):   # 첫줄 찾기
        for x in range(xlen):
            if '.' == wallpaper[y][x]:
                continue
            answer[0],answer[2] = y,y
            answer[1] = x       # 작은 x

            for maxX in range(xlen-1,x-1,-1):  # 큰 x
                if wallpaper[y][maxX] == "#":
                    answer[3] = maxX
                    break

            flag = True
            break
        if flag:
            break

    for y in range(answer[0]+1,len(wallpaper)): # 첫줄 후 부터 끝까지 검사
         for x in range(xlen):
            if '.' == wallpaper[y][x]:
                continue
            answer[2] = y
            if answer[1] > x:
                answer[1] = x

            for maxX in range(xlen-1,x-1,-1):
                if wallpaper[y][maxX] == "#":
                    if answer[3] < maxX:
                        answer[3] = maxX
                    break
    answer[2] += 1
    answer[3] += 1

    return answer


