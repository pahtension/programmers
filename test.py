l = [[3,4,2],[5,9,7]]
# print(({2,3,1,2}-{2,3}).pop())

# s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
# "".re
# # ss = []
# print(s[:0]+s[1+1:])
# print(int(not "2"))
# a = 1
# print([i for i in range(10)])
def solution(numbers):
    numbers.sort()
    return numbers.pop()*numbers.pop()
print(solution([1,2,3,4]))
# for i in (s[1:-1]+",").split("{")[1:]:
#     print(list(map(int, i[:-2].split(","))))
# for i in range(10):
#     if i==7:
#         i+=1
#     print(i)
