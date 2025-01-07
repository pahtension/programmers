import math
import time

start = time.time()
#여기 부터

# l = [i for i in range(1000000)]
l=set()
for i in range(1000000):
    l.add(i)


print(max(l))

#여기까지
end = time.time()

print(f"{end - start} sec")

# 출처: https://blockdmask.tistory.com/549 [개발자 지망생:티스토리]