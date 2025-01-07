# 이웃한 칸  https://school.programmers.co.kr/learn/courses/30/lessons/250125

def solution(board, h, w):
    answer = 0
    lenght = len(board)
    for a,b in ((-1,0),(1,0),(0,1),(0,-1)):
        dh,dw =h+a,w+b
        answer += 0<=dh<lenght and 0<=dw<lenght and board[h][w] == board[dh][dw]
    return answer