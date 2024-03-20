#col = alphabet, row = int
loc = list(input()) #loc[0] = col, loc[1] = row
cols = ['a','b','c','d','e','f','g','h']
for i, c in enumerate(cols):
  if c == loc[0]:
    curr_col = i+1
    break
curr_row = int(loc[1])

def isPossible(col, row):
  if col > 0 and row >0 and col <=8 and row<=8:
    return 1
  return 0

dcol = [2, 2, 1, -1, -2,-2, 1,-1]
drow = [1, -1, 2, 2, 1,-1, -2,-2]
# 0 < curr_row, curr_col <= 8

cnt = 0
for i in range(8):
  cnt += isPossible(curr_col+dcol[i], curr_row+drow[i])

print(cnt)