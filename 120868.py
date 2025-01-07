def solution(sides):
    small,big = sorted(sides)
    return len(range(big-small+1,small+big))

print(solution([11,7]))