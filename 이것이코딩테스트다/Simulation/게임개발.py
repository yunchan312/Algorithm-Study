rows, cols = map(int, input().split())
c_row, c_col, direction = map(int, input().split())
plate = [list(map(int, input().split())) for _ in range(rows)]

dx=[-1,0,1,0]
dy=[0,-1,0,1]

def canMove(plate, r, c):
  global dx, dy
  for i in range(4):
    if plate[r+dy[i]][c+dx[i]] == 0:
      return True
  return False



plate[c_row][c_col] = 1
cnt = 1
while(True):
  direction += 1
  direction %= 4
  
  if not canMove(plate, c_row, c_col):
    break
  if plate[c_row+dy[direction]][c_row+dy[direction]] == 0:
    cnt += 1
    c_row += dy[direction]
    c_col += dx[direction]
    plate[c_row][c_col] = 1
print(cnt)