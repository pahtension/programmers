def solution(s, n):
    answer = ''
    for i in s:
        if i == ' ':
            answer+=" "
            continue
        m = ord(i)
        z = 65 if m < 91 else 97
        answer += chr((m-z+n)%26+z)
        
    return answer

print(solution("z B",1))
print(ord("a"))
