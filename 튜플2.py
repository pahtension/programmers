def solution(s):

    answer = []
    lenght = 0
    nlist = {0:set()}

    for i in (s[1:-1]+",").split("{")[1:]:
        l = list(map(int, i[:-2].split(",")))
        le = len(l)
        nlist[le] = set(l)

        if lenght< le:
            lenght = le
    

    for i in range(1,lenght+1):
        answer.append((nlist[i] - nlist[i-1]).pop())
    
    return answer

print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))