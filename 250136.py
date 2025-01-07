from collections import deque


def solution(land):
    land2 = [0]+[0  for i in land[0]]+[0] #각 x좌표마다 매장된 석유량
    land = [land2[::]]+ [[0]+i+[0] for i in land]+[land2[::]] #판 위아래 양옆 한칸씩 늘리기

    print("원본") # 프린트
    for k in land:
        for m in k:
            print(m,end=" ")
        print()
    print()

    check = set() # 검사한 좌표
    checkLen = 0
    ol = deque()
    jlen = len(land[0])
    for i in range(1,len(land)-1):
        for j in range(1,jlen):
            if land[i][j]:
                land[i][j] = 0
                oil = 1
                ol.append((i,j))
                xl = set(j)

                for k in land: # 프린트
                    for m in k:
                        print(m,end="\t")
                    print()
                print()

                while(len(ol)):
                    print(f"ol {ol}") # 프린트
                    y,x = ol.pop()
                    xyList = ((y-1,x),(y+1,x),(y,x-1))
                    for yy,xx in xyList:
                        if land[yy][xx]:
                            land[yy][xx] = 0
                            oil += 1
                            check.add((yy,xx))
                            if len(check) != checkLen:
                                ol.append((yy,xx))
                    x+=1
                    if land[y][x] :
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
                    print(xyList,y,x) 


                land2[j] += oil #누적합
                land2[max(xl)+1] -= oil

    print(land2)
    for i in range(1,jlen-1): #누적합 적용
        land2[i+1] += land2[i]
    print(land2)
    return max(land2)


print(solution([[0, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 1, 1, 0, 0], [1, 1, 0, 0, 0, 1, 1, 0], [1, 1, 1, 0, 0, 0, 0, 0], [1, 1, 1, 0, 0, 0, 1, 1]]))