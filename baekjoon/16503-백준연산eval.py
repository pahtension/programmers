#https://www.acmicpc.net/problem/16503
li = input().split()

a = int(eval(str(int(eval("".join(li[0:3]))))+li[3]+li[4]))
b = int(eval(li[0]+li[1]+str(int(eval("".join(li[2:5]))))))
print(min(a,b))
print(max(a,b))
