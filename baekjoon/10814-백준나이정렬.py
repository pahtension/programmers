
print(*[' '.join(l) for l in sorted(
    [input().split() for _ in range(int(input()))]
    ,key=lambda x:int(x[0]))],sep='\n')