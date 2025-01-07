#https://www.acmicpc.net/problem/32964
n = int(input())
up = input()
down = input()

f=0
board = (up,down)

for y,x,p in ((0,1,1),(1,0,0)): #p 1 가로 0 새로 
    while True:
        if x == n :
            break
        m = board[y][x]
        if m == "X":
            f = 1
            break
        if m == "L":
            if p:
                y = not y
                p = 0
            else:
                x+=1
                p = 1
        else:
            if p:
                x+=1
            else:
                break

    if f:
        break



print("YES"if f else"NO")
