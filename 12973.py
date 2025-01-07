from collections import deque

def solution(s):
    answer = 1
    i = 1
    
    popL = deque()
    while i<len(s):
        if s[i] == s[i-1]:
            s= s[:i-1]+s[i+1:]
            popL.append(i-1)
            print(s,i-1)
            continue
        i+=1

    while popL:

        zg = 0
        if popL[0] == 0:
            popL.popleft()
        popL2 = deque()
        for i in popL:
            i+=zg
            if i>len(s)-1: 
                break
            if s[i] == s[i-1]:
                s = s[:i-1]+s[i+1:]
                popL2.append(i-1)
                print(s,i-1)
                zg-=2

        popL = popL2


    return int(not s)

print(solution("baabaa"))
