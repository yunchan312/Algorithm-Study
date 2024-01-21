'''단지번호붙이기'''

n = int(input())
apt = []
houses = []

for i in range(n):
    apt.append(list(map(int, input())))

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def setting(y, x):
    if x < 0 or x>=n or y<0 or y>=n:
        return False
    if apt[y][x] == 1:
        global h
        h +=1
        apt[y][x] = 0
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            setting(ny, nx)
        return True
    return False

cnt = 0
h = 0
for i in range(n):
    for j in range(n):
        if setting(j,i) == True:
           houses.append(h)
           cnt +=1
           h = 0
houses.sort()
print(cnt)
for i in houses:
    print(i)