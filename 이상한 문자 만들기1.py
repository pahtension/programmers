def solution(s):
    answer = []
    l = ((0,-32),(32,0))
    for i in s.split(" "):
        st = ""
        for n,j in enumerate(i):
            m = ord(j)
            st += chr(m+l[n%2][int(m > 91)])
        answer.append(st)
    return " ".join(answer)

print(solution("try hello   world  "))