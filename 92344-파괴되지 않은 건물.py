# 파괴되지 않은 건물  https://school.programmers.co.kr/learn/courses/30/lessons/92344

def solution(board, skill):
  a,b = len(board),len(board[0])
  dboard = [[0 for j in range(b+1)] for i in range(a+1)]
  for i in skill:
    if i[0]==1:
      i[5] *= -1

    dboard[i[1]][i[2]] += i[5]
    dboard[i[3]+1][i[2]] -= i[5]
    dboard[i[1]][i[4]+1] -= i[5]
    dboard[i[3]+1][i[4]+1] += i[5]

  for i in range(a):
    for j in range(b):
      dboard[i][j+1] += dboard[i][j]
  for i in range(b):
    for j in range(a):
      dboard[j+1][i] += dboard[j][i]
  
  
  for i in range(a):
    for j in range(b):
      board[i][j] += dboard[i][j]

  return len([j for i in board for j in i if j >0])

