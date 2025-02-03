#15953 상금헌터

# l = []
# for i in range(int(input())):
#     l.append(map(int,input().split()))

# d1 = [0]+[5000000]+ [3000000]*2 + [2000000]*3 +[500000]*4+[300000]*5+[100000]*6 + [0]*80
# d2 = [0]+[5120000]+ [2560000]*2 + [1280000]*4 + [640000]*8 + [320000]*16 + [0]*33

# for i1,i2 in l:
#     print(d1[i1]+d2[i2])

#15954 표준편차 https://www.acmicpc.net/problem/15954

import math

N,K =map(int,input().split())

nl = list(map(int,input().split()))

min_boon = float('inf')
result = 0

for cnt in range(K, N+1): 
    total = sum(nl[:cnt])
    total_sq = sum(x ** 2 for x in nl[:cnt])
    
    boon = total_sq - (total ** 2) / cnt
    if boon < min_boon:
        min_boon = boon
        result = math.sqrt(boon / cnt)
    
    for i in range(cnt, N):
        total += nl[i] - nl[i - cnt]
        total_sq += nl[i] ** 2 - nl[i - cnt] ** 2
        
        boon = total_sq - (total ** 2) / cnt
        if boon < min_boon:
            min_boon = boon
            result = math.sqrt(boon / cnt)

print(result)



import decimal

# 입력
N, K = map(int, input().split())
nl = list(map(int, input().split()))
min_boon = decimal.Decimal('inf')
result = decimal.Decimal(0)

# 처음 K 크기 계산
total = [decimal.Decimal(sum(nl[:K]))]   # [5+4+3]->[5+4+3+2+1, 4+3+2+1, 3+2+1]
total_sq = [decimal.Decimal(sum(x ** 2 for x in nl[:K]))]

# 분산 계산
boon = total_sq[0] - decimal.Decimal(total[0] ** 2) / decimal.Decimal(K)
min_boon = boon
result = decimal.Decimal(decimal.Decimal(boon) / decimal.Decimal(K)).sqrt()

for i in range(K, N):
    # 슬라이딩 윈도우 적용할 K크기 총합 복사, 앞에 값 빼기
    total.append(total[-1])
    total_sq.append(total_sq[-1])
    
    total[-1] -= nl[i - K]
    total_sq[-1] -= nl[i - K] ** 2

    for j in range(len(total)):
        # 뒷 값 추가
        total[j] += nl[i] 
        total_sq[j] += nl[i] ** 2 

        boon = total_sq[j] - decimal.Decimal(total[j] ** 2) / decimal.Decimal(K+len(total)-j-1)
        if boon < min_boon:
            min_boon = boon
            result = decimal.Decimal(boon / decimal.Decimal(K+len(total)-j-1)).sqrt()

print(result)
