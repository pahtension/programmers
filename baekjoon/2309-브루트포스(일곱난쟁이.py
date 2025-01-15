p =[]
for i in range(9):
    p.append(int(input()))

s = sum(p)
n1,n2 = 0,0
endFlag =False
for i in range(9):
    for j in range(8,i,-1):
        if s-p[i]-p[j]==100:
            n1,n2=i,j
            endFla=True
            break
    if endFlag:
        break

p2=[]
for i in range(9):
    if i==n1 or i==n2:
        continue
    p2.append(p[i])

print("\n".join(map(str,sorted(p2))))