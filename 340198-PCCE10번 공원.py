#[PCCE 기출문제] 10번 / 공원  https://school.programmers.co.kr/learn/courses/30/lessons/340198

def solution(mats, park):
    mats.sort() # 작은 사이즈 부터 탐색
    mats.append(52) # mats 를 pop 할거라 park보다 큰값 추가
    answer = -1 
    x,y = 0,0
    while True:
        if park[y][x] == '-1':  # -1 발견
            fg1 = False         # -1 외 발견시 True
            for i in mats:      # 작은 사이즈 부터 탐색
                if len(park[0]) < x+i or len(park) < y+i : # 찾을 사이즈 공간 안나오면 break
                    break
                for py in range(i):
                    for px in range(i):
                        if park[y+py][x+px] != "-1":    # -1 아닌거 발견 for문 모두 종료
                            fg1 = True
                            break
                    if fg1:
                        break
                if fg1:
                    break
                else:   # 해단 사이즈 내에 다른 돗자리가 없었을때
                    answer = mats.pop(0) # answer에 적제 후 해당 사이즈 리스트에서 삭제

        x += 1   
        if len(park[0]) < x+mats[0] :   # x
            x = 0
            y += 1
        if len(park) < y+mats[0] :      # y
            break

    return answer
