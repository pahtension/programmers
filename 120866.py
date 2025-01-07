
def solution(board):
    l = ((-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,-1),(1,0),(1,1))
    leng = len(board)
    dlist = set()
    for i in range(leng):
        for j in range(leng):
            if board[i][j]:
                dlist.add((i,j))

    for x,y in tuple(dlist):
        for zx,zy in l:
            dx,dy = x+zx, y+zy
            if 0<=dx<leng and 0<=dy<leng:
                dlist.add((dx,dy))

    return leng**2 - len(dlist)

print(solution([[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 0, 0]]))