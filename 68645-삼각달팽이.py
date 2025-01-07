#https://school.programmers.co.kr/learn/courses/30/lessons/68645

def solution(n):
    answer = [[0 for j in range(i+1)] for i in range(n)]
    l = ((1,0),(0,1),(-1,-1))
    li = 0
    num = 1
    y,x = -1,0
    for i in range(n,0,-1):
        dy,dx = l[li%3]
        li+=1
        for j in range(i):
            y,x = y+dy, x+dx
            answer[y][x] = num
            num+=1
    ans = []
    for i in answer:
        ans+=i
    return ans
print(solution(4))