n = int(input())
directions = list(input().split())

#(row, col)
cy, cx = 1,1 # 1 <= cx, cy <= n

for d in directions:
  if d == 'R' and cx+1 <=n:
    cx += 1
  elif d == 'U' and cy-1>0:
    cy -= 1
  elif d == 'L' and cx-1>0:
    cx-=1
  elif d =='D' and cy+1<=n:
    cy += 1
  
print(cy, cx)

