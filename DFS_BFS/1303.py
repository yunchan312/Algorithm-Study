'''전쟁-전투'''

#왜 오류뜨는지 모르겠음 ㄹㅇ
n,m = map(int, input().split())
war = [input() for _ in range(m)]
visited = [[False for _ in range(n)] for _ in range(m)]

dx=[0,0,-1,1]
dy=[-1,1,0,0]
blue = []
b=0
white = []
w=0

def getPower(y,x,color):
    if y<0 or y>=m or x<0 or x>=n:
        return False
    if war[y][x] == color and not visited[y][x]:
        visited[y][x] = True
        global b,w
        if color == 'B':
            b +=1
        else:
            w +=1
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            getPower(ny, nx, color)
        return True
    return False

for i in range(m):
    for j in range(n):
        if getPower(j,i,'B') == True:
            blue.append(b**2)
            b = 0
        if getPower(j,i,'W') == True:
            white.append(w**2)
            w = 0

print(sum(white), sum(blue))