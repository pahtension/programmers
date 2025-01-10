# 백준 https://www.acmicpc.net/problem/15665

n,m = input().split()
n = sorted(map(int,set(input().split()))) #중복 삭제, 정렬
lenN = len(n)

i = [0]*int(m)  # n 리스트 반복용 인덱스
m = range(len(i)-1,0,-1) # i 검사(올림)

while True:
    
    s=[]
    for j in i:
        s.append(n[j])
    print(*s,end="")

    i[-1] += 1
    for j in m:  # i 검사(올림)
        if i[j] == lenN:
            i[j]=0
            i[j-1]+=1
        else:
            break
    if i[0]==lenN:
        break
    print()



