def solution(rows, columns, queries):
    board =[[j+1+i*columns for j in range(columns)] for i in range(rows)]
    
    for i in board:
        for j in i:
            print(j,end=" ")
        print()

    answer = []
    queries = [[j-1 for j in i] for i in queries]
    for q in queries:
        min = rows*columns
        y,x = q[0],q[1]
        num = board[y][x]
        while(x!=q[3]):
            x+=1
            num,board[y][x] = board[y][x],num
            if min>num:
                min = num
        while(y!=q[2]):
            y+=1
            num,board[y][x] = board[y][x],num
            if min>num:
                min = num
        while(x!=q[1]):
            x-=1
            num,board[y][x] = board[y][x],num
            if min>num:
                min = num
        while(y!=q[0]):
            y-=1
            num,board[y][x] = board[y][x],num
            if min>num:
                min = num
        answer.append(min)
        
    
    
    return answer

print(solution(3,3,[[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]]))