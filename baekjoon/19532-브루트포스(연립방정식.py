a,b,c,d,e,f = map(int,input().split())

endFlag = False
xx,yy = 0,0
for x in range(-999,1000):
    for y in range(-999,1000):
        if a*x+b*y == c and d*x+e*y == f:
            xx,yy = x,y
            endFlag = True
            break
    if endFlag:
        break

print(xx,yy)