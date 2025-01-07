# [PCCP 기출문제] 2번 / 석유 시추  https://school.programmers.co.kr/learn/courses/30/lessons/250136

from collections import deque

def solution(land):
    low,col =len(land), len(land[0])
    land2 = [0]*(col+1) #각 x좌표마다 매장된 석유량


    print("원본") # 프린트
    for k in land:
        for m in k:
            print(m,end=" ")
        print()
    print()

    check = set() # 검사한 좌표
    checkLen = 0
    ol = deque()

    for i in range(low):
        for j in range(col):
            if land[i][j]:
                land[i][j] = 0
                oil = 1
                ol.append((i,j))
                xl = {j}

                for k in land: # 프린트
                    for m in k:
                        print(m,end="\t")
                    print()
                print()

                while(len(ol)):
                    print(f"ol {ol}") # 프린트
                    y,x = ol.pop()
            

                    y-=1
                    if 0<=y and land[y][x]:
                        land[y][x] = 0
                        oil += 1
                        check.add((y,x))
                        if len(check) != checkLen:
                            ol.append((y,x))
                    y+=2
                    if y<low and land[y][x]:
                        land[y][x] = 0
                        oil += 1
                        check.add((y,x))
                        if len(check) != checkLen:
                            ol.append((y,x))
                    y-=1
                    x-=1
                    if  0<=x and land[y][x] :
                        land[y][x] = 0
                        oil += 1
                        check.add((y,x))
                        if len(check) != checkLen:
                            ol.append((y,x))
                    x+=2
                    if  x<col and land[y][x] :
                        land[y][x] = 0
                        oil += 1
                        check.add((y,x))
                        if len(check) != checkLen:
                            ol.append((y,x))
                        xl.add(x)

                    for k in land: # 프린트
                        for m in k:
                            print(m,end="\t")
                        print()
                    print(y,x) 


                land2[j] += oil #누적합
                land2[max(xl)+1] -= oil

    print(land2)#
    for i in range(col): #누적합 적용
        land2[i+1] += land2[i]

    print(land2)#
    return max(land2)


print(solution([[0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [1, 1, 0, 0, 0, 1, 1, 0], [1, 1, 1, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 1, 1]]))