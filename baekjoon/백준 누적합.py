

# 2851 마리오
p =[]
for i in range(10):
    p.append(int(input()))

n1 = n2 = 0
for i in p:
    n2+=i
    if abs(n2-100) <= abs(n1-100):
        n1 = n2
    if n2>=100:
        break
print(n1)


# 구간 합 11659
length,n = input().split()
nl = input().split()
sl =[]
for i in range(int(n)):
    sl.append(input().split())

hl =[0]

for i in nl:
    hl.append(hl[-1]+int(i))

for s,e in sl:
    print(hl[int(e)]-hl[int(s)-1])


#🎵니가 싫어 싫어 너무 싫어 싫어 오지 마 내게 찝쩍대지마🎵      -모기 20440

room = {} 
for i in range(int(input())):
    s,e=map(int,input().split())
    room[s]=room.get(s,0)+1
    room[e]=room.get(e,0)-1

mg = 0   
startI = 0
endI = 0
maxN = 0
maxF = False
for i in sorted(room.keys()):
    mg += room[i]
    if mg>maxN:
        maxN = mg
        startI = i
        maxF = True
    elif maxF:
        if mg<maxN:
            endI = i
            maxF = False

print(maxN)
print(startI,endI)


